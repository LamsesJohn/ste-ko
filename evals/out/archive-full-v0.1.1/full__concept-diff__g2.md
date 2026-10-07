결론: 둘 다 한 브랜치의 변경을 다른 브랜치에 합친다. merge는 히스토리를 그대로 보존하고, rebase는 히스토리를 다시 쓴다.

## 동작 방식

- **merge**는 두 브랜치를 잇는 머지 커밋을 새로 만든다. 기존 커밋은 바뀌지 않는다.
- **rebase**는 내 커밋을 대상 브랜치 끝에 하나씩 다시 적용한다. 이때 커밋 해시가 새로 만들어진다.

```bash
# merge: main의 변경을 feature에 합친다
git switch feature
git merge main

# rebase: feature의 커밋을 main 끝으로 옮긴다
git switch feature
git rebase main
```

## 비교

| 항목 | merge | rebase |
|---|---|---|
| 히스토리 모양 | 분기와 합류가 보인다 | 일직선이다 |
| 기존 커밋 | 바뀌지 않는다 | 해시가 바뀐다 |
| 머지 커밋 | 생긴다 | 생기지 않는다 |
| 충돌 해결 | 한 번에 한다 | 커밋마다 할 수 있다 |
| 되돌리기 | 쉽다 | 상대적으로 어렵다 |

## 선택 기준

- 이미 push해서 다른 사람이 쓰는 브랜치에는 rebase를 쓰지 않는다. 해시가 바뀌어 다른 사람의 히스토리와 어긋난다.
- 내 로컬 브랜치를 정리하거나 최신 main 위에 올릴 때는 rebase가 깔끔하다.
- 공유 브랜치에 합칠 때는 merge가 안전하다.

rebase한 브랜치를 이미 push했다면 `git push --force-with-lease`가 필요하다. 이 명령은 원격 히스토리를 덮어쓰므로 팀에 먼저 알린다.
