원격 `main`에 내 로컬에 없는 커밋이 있어서 push가 거부됐습니다. 먼저 원격 변경을 가져와 합친 뒤 다시 push하면 됩니다.

이 디렉터리는 git 저장소가 아니어서 상태는 직접 확인하지 못했습니다. 아래는 일반적인 해결 절차입니다.

1. 원격 변경을 확인합니다.
   ```
   git fetch origin
   git log --oneline HEAD..origin/main
   ```
2. 합치는 방법을 하나 고릅니다.

   | 방법 | 명령 | 결과 |
   |---|---|---|
   | rebase | `git pull --rebase origin main` | 히스토리가 한 줄로 유지됩니다. |
   | merge | `git pull origin main` | 병합 커밋이 생깁니다. |

3. 충돌이 나면 파일을 수정한 뒤 이어서 진행합니다.
   ```
   git add <파일>
   git rebase --continue
   ```
4. 다시 push합니다.
   ```
   git push origin main
   ```

`git push --force`는 쓰지 않는 것이 좋습니다. 다른 사람의 커밋을 원격에서 지울 수 있습니다.

실제 저장소 경로를 알려주면 `git status`와 `git log`로 상태를 확인하고 더 구체적으로 안내하겠습니다.
