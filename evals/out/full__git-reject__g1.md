원격 `main`에 내 로컬에 없는 커밋이 있어서 push가 거절되었습니다. 원격 변경을 먼저 가져와 합친 뒤 다시 push하면 됩니다.

```
! [rejected] main -> main (non-fast-forward)
```

1. 원격 변경을 가져와 내 커밋 아래에 다시 쌓습니다.
   ```
   git pull --rebase origin main
   ```
2. 충돌이 나면 표시된 파일을 고칩니다. 그다음 아래 명령을 실행합니다.
   ```
   git add <파일>
   git rebase --continue
   ```
3. 다시 push합니다.
   ```
   git push origin main
   ```

rebase 대신 merge 커밋을 남기고 싶으면 1번을 `git pull origin main`으로 바꿉니다.

`git push --force`는 쓰지 않습니다. 원격에 있는 다른 사람의 커밋이 사라집니다.

저는 이 저장소의 상태를 확인하지 못했습니다. 원격에 어떤 커밋이 있는지 보려면 `git fetch` 후 `git log HEAD..origin/main`을 실행합니다.
