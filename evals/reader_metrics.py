#!/usr/bin/env python3
"""Reader-visible metrics for Korean replies. Standard library only.

Counts what a reader sees: sentence length in eojeol (space-separated tokens),
dashes, semicolons, bold spans, headers, list items, table rows, and stock phrases.
List items and table rows count as sentences, so splitting a long sentence into
a list does not hide it.

Usage:
    reader_metrics.py FILE [FILE ...] [--max-eojeol 25] [--json] [--check]
    echo "텍스트" | reader_metrics.py [--json]

--check exits 1 when a hard violation exists:
a sentence over the limit, an em dash, a semicolon, an opener, or a closer.
The numbers measure form. They do not measure quality.
"""
import argparse
import json
import re
import sys

OPENERS = [
    r"좋은 질문", r"훌륭한 질문", r"살펴보겠습니다", r"알아보겠습니다",
    r"물론입니다", r"안녕하세요",
]
CLOSERS = [
    r"도움이 (되길|되었으면)", r"말씀해 주세요", r"편하게 (물어|말씀)",
    r"궁금한 (점|것)이 (있으시면|있으면)", r"추가로 (궁금|필요)",
]
STOCK = [
    r"강력한", r"혁신적", r"획기적", r"원활하게", r"매끄럽게", r"효율적으로",
    r"다양한", r"중요합니다", r"핵심적",
]
NOMINALIZATION = [
    r"[을를] 수행", r"[을를] 실시", r"[을를] 진행", r"이루어(진|지)", r"되어지",
]

FENCE = re.compile(r"```.*?```", re.S)
SENT_END = re.compile(r"(?<=[.!?。])\s+")
LIST_MARK = re.compile(r"^\s*([-*]|\d+[.)])\s+")


def strip_code(text):
    """Remove fenced code blocks. Keep inline code."""
    return FENCE.sub("\n", text)


def split_sentences(text):
    """Split on sentence marks and on line breaks. A list item is a sentence."""
    out = []
    for line in strip_code(text).splitlines():
        line = LIST_MARK.sub("", line).strip().strip("|").strip()
        if not line or re.fullmatch(r"[-| :]+", line):
            continue
        for part in SENT_END.split(line):
            part = part.strip()
            if part:
                out.append(part)
    return out


def count_hits(patterns, text):
    return sum(len(re.findall(p, text)) for p in patterns)


def analyze(text, max_eojeol=25):
    body = strip_code(text)
    sentences = split_sentences(text)
    lengths = [len(s.split()) for s in sentences]
    over = [n for n in lengths if n > max_eojeol]
    return {
        "eojeol": sum(lengths),
        "sentences": len(sentences),
        "avg_eojeol_per_sentence": round(sum(lengths) / len(lengths), 1) if lengths else 0.0,
        "max_eojeol_in_sentence": max(lengths) if lengths else 0,
        "sentences_over_limit": len(over),
        "em_dash": body.count("—"),
        "semicolon": body.count(";"),
        "bold_spans": len(re.findall(r"\*\*[^*\n]+\*\*", body)),
        "headers": len(re.findall(r"^\s*#{1,6}\s", body, re.M)),
        "list_items": len(re.findall(r"^\s*([-*]|\d+[.)])\s+", body, re.M)),
        "table_rows": len(re.findall(r"^\s*\|", body, re.M)),
        "openers": count_hits(OPENERS, body),
        "closers": count_hits(CLOSERS, body),
        "stock_phrases": count_hits(STOCK, body),
        "nominalizations": count_hits(NOMINALIZATION, body),
    }


def hard_violations(m):
    return (m["sentences_over_limit"] + m["em_dash"] + m["semicolon"]
            + m["openers"] + m["closers"])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="*")
    ap.add_argument("--max-eojeol", type=int, default=25)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)

    inputs = []
    if args.files:
        for path in args.files:
            with open(path, encoding="utf-8") as f:
                inputs.append((path, f.read()))
    else:
        inputs.append(("<stdin>", sys.stdin.read()))

    results = {name: analyze(text, args.max_eojeol) for name, text in inputs}
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for name, m in results.items():
            print(f"== {name}")
            for k, v in m.items():
                print(f"  {k}: {v}")
    if args.check and any(hard_violations(m) for m in results.values()):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
