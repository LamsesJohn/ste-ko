# ste-ko

한국어 답변과 문서를 ASD-STE100의 원칙으로 쓰게 하는 에이전트 스킬이다.
Claude Code, Codex, Grok 같은 `SKILL.md` 형식을 읽는 도구에서 쓴다.

English summary: a Korean adaptation of the SimpleEnglish skill (MIT). It makes an agent write Korean replies and documents with short sentences, one fact per sentence, active voice, and one word per concept. It is not affiliated with ASD and does not certify STE compliance.

## 무엇을 하는가

- 모든 채팅 답변에 규칙 10개를 적용한다. 첫 문장에 결론을 쓰고, 한 문장에 한 동작만 쓰고, 문장은 25어절 이하로 쓴다.
- 문서, README, 런북, 보고서에는 규칙 12개를 더한다. 피동과 명사화를 줄이고, 용어 표기를 고정하고, 상투 표현을 쓰지 않는다.
- 답변에서 목록과 표를 허용한다. 순서가 있는 절차는 번호 목록으로, 같은 속성의 비교는 표로 쓴다.
- 확인한 것과 확인하지 못한 것을 구분한다. 원문에 없는 수치와 원인을 만들지 않는다.

## 바탕과 차이

[AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish)(MIT)의 구조를 한국어로 옮겼다. 자세한 내용은 [NOTICE.md](NOTICE.md)에 있다.

| 항목 | SimpleEnglish | ste-ko |
|---|---|---|
| 언어 | 영어 | 한국어 |
| 답변 형식 | 산문만 | 목록과 표 허용 |
| 길이 기준 | 단어 수 | 어절 수 |
| 영어 전용 규칙(시제, 조동사, 구동사) | 있음 | 없음 |
| 한국어 규칙(피동, 명사화, 종결어미, 용어 표기) | 없음 | 있음 |
| Strict 모드(ASD 어휘) | 있음 | 없음 |

## 설치

스킬 폴더 `skills/ste-ko`를 도구의 스킬 위치에 복사한다.

| 도구 | 프로젝트 위치 | 사용자 위치 |
|---|---|---|
| Claude Code | `.claude/skills/ste-ko` | `~/.claude/skills/ste-ko` |
| Codex | `.agents/skills/ste-ko` | `~/.agents/skills/ste-ko` 또는 `~/.codex/skills/ste-ko` |
| Grok | `.grok/skills/ste-ko` 또는 `.agents/skills/ste-ko` | `~/.grok/skills/ste-ko` |

- Grok의 위치는 Grok 사용자 가이드에서 확인했다. Claude Code 위치는 공식 방식이다. Codex 위치는 제3자 문서에서 확인했고 직접 시험하지 않았다.
- 스킬은 모델이 필요하다고 판단할 때 읽힌다. 모든 답변에 확실히 적용하려면 지침 파일(`AGENTS.md`, `CLAUDE.md`)에 핵심 규칙을 함께 쓴다.

지침 파일에 넣는 핵심 규칙 예시:

```markdown
## 답변 문체 (ste-ko)

- 첫 문장에 결론을 쓴다. 한 문장에는 동작이나 사실을 하나만 쓴다.
- 설명 문장은 25어절 이하, 절차 문장은 20어절 이하로 쓴다.
- 능동태로 쓴다. 한 대상에는 한 단어만 쓴다.
- 줄표(—)와 세미콜론(;)을 쓰지 않는다. 인사말과 맺음말을 쓰지 않는다.
- 확인한 것과 확인하지 못한 것을 구분한다. 확신 수준을 바꾸지 않는다.
- 절차는 번호 목록, 비교는 표로 쓴다. 코드와 경로와 인용문은 그대로 둔다.
```

## 측정

`evals/reader_metrics.py`는 답변의 형태를 센다. 어절 수, 문장 길이, 줄표, 세미콜론, 굵은 글씨, 제목, 목록, 표, 인사말, 상투 표현, 명사화를 센다. 목록 항목과 표 행도 문장으로 센다.

```bash
python3 evals/reader_metrics.py reply.md
python3 evals/reader_metrics.py --check reply.md   # 위반이 있으면 종료 코드 1
python3 -m unittest evals/test_reader_metrics.py   # 테스트
```

- 이 수치는 형태만 잰다. 글의 품질을 재지 않는다.
- `evals/scenarios.json`에 시험 시나리오 8개가 있다. 규칙 없음, 짧은 규칙, 전체 스킬을 같은 시나리오로 비교한다.
- 효과를 실제로 측정한 결과는 아직 없다.

## 한계

- 이 스킬은 ASD-STE100 준수를 보증하지 않는다. ASD의 어휘 사전도 싣지 않는다.
- ASD가 승인하거나 보증한 제품이 아니다.
- 마케팅, 문학, 설득이 목적인 글에는 쓰지 않는다.
- 법령과 계약처럼 문구가 정해진 글은 원문을 바꾸지 않는다.

## 라이선스

MIT. 원본 저작권 고지를 유지한다. [LICENSE](LICENSE)와 [NOTICE.md](NOTICE.md)를 본다.
