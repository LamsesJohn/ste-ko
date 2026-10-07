`git merge`는 두 브랜치의 히스토리를 보존한 채 합치고, `git rebase`는 내 커밋을 다른 브랜치 끝으로 옮겨 히스토리를 한 줄로 만듭니다.

| 항목 | merge | rebase |
|---|---|---|
| 히스토리 | 분기와 합류가 그대로 남음 | 직선 형태로 재작성됨 |
| 새 커밋 | 머지 커밋이 하나 생김 | 머지 커밋이 생기지 않음 |
| 기존 커밋 | 해시가 바뀌지 않음 | 해시가 새로 만들어짐 |
| 충돌 처리 | 한 번에 해결함 | 커밋마다 해결할 수 있음 |
| 공유 브랜치 | 안전함 | 이미 push한 커밋에는 위험함 |
| 되돌리기 | 머지 커밋 하나를 revert하면 됨 | reflog로 복구해야 함 |

## 동작 예시

`feature` 브랜치에서 `main`의 변경을 가져오는 경우입니다.

```bash
# merge
git switch feature
git merge main

# rebase
git switch feature
git rebase main
```

merge는 `feature`에 머지 커밋을 추가합니다. rebase는 `feature`의 커밋을 `main` 최신 지점 위에 다시 만듭니다.

## 선택 기준

1. 이미 push했거나 다른 사람이 쓰는 브랜치에는 merge를 씁니다.
2. 내 로컬 작업 브랜치를 최신 `main`에 맞출 때는 rebase를 씁니다.
3. 실제 합류 이력을 남기고 싶으면 merge를 씁니다.
4. 읽기 쉬운 선형 로그를 원하면 rebase를 씁니다.
5. push한 브랜치를 rebase했다면 `git push --force-with-lease`가 필요합니다. 팀과 먼저 합의해야 합니다.

## 팁

`git rebase -i`를 쓰면 커밋을 합치거나 순서를 바꾸거나 메시지를 고칠 수 있습니다. rebase 도중 문제가 생기면 `git rebase --abort`로 원래 상태로 돌아갑니다.
