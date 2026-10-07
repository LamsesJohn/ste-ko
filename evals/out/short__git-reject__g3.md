원격 `main`에 내 로컬에 없는 커밋이 있어서 push가 거부됐습니다. 먼저 원격 변경을 가져와 합친 뒤 다시 push하면 됩니다.

현재 작업 디렉터리는 git 저장소가 아니어서 상태를 직접 확인하지 못했습니다. 아래 절차는 push를 실행한 저장소 안에서 실행하세요.

1. 원격 변경을 가져와 내 커밋을 그 위로 옮깁니다.
   ```
   git pull --rebase origin main
   ```
2. 충돌이 나면 파일을 고치고 아래 명령을 실행합니다.
   ```
   git add <파일>
   git rebase --continue
   ```
3. 다시 push합니다.
   ```
   git push origin main
   ```

rebase 대신 merge 커밋을 원하면 1번을 `git pull origin main`으로 바꾸세요.

`git push --force`는 쓰지 마세요. 원격에 있는 다른 사람의 커밋이 사라질 수 있습니다.

원격에 어떤 커밋이 있는지 먼저 보고 싶으면 아래 명령을 쓰세요.

```
git fetch origin
git log HEAD..origin/main --oneline
```
