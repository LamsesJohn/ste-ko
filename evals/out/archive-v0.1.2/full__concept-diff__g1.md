`merge`는 두 브랜치의 기록을 그대로 두고 합치는 커밋을 만듭니다. `rebase`는 내 커밋을 대상 브랜치의 끝으로 옮겨 다시 만듭니다.

| 항목 | merge | rebase |
|---|---|---|
| 기록 모양 | 갈라졌다 합쳐지는 형태 | 일직선 |
| 새 커밋 | 병합 커밋 1개 | 없음 (기존 커밋이 새 해시로 다시 만들어짐) |
| 기존 커밋의 해시 | 바뀌지 않음 | 바뀜 |
| 충돌 해결 | 한 번에 | 커밋마다 필요할 수 있음 |
| 되돌리기 | 쉬움 | 상대적으로 어려움 |

## 명령

```bash
# merge: main에 feature를 합친다
git switch main
git merge feature

# rebase: feature를 main 끝으로 옮긴다
git switch feature
git rebase main
```

## 선택 기준

- 이미 push한 공유 브랜치에는 `rebase`를 쓰지 않습니다. 해시가 바뀌어서 다른 사람의 기록과 어긋납니다.
- 아직 나만 쓰는 로컬 브랜치를 최신 `main` 위로 정리할 때는 `rebase`를 씁니다.
- 브랜치가 언제 합쳐졌는지 기록으로 남기고 싶으면 `merge`를 씁니다.
- 기록을 일직선으로 유지하는 팀 규칙이 있으면 `rebase`를 씁니다.

## 주의

`rebase` 뒤에 이미 push한 브랜치를 올리려면 `git push --force-with-lease`가 필요합니다. 강제 push는 원격 기록을 덮어씁니다. 공유 브랜치에서는 하지 않습니다.
