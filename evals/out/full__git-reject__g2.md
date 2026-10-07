원격 `main`에 내 로컬에 없는 커밋이 있어서 push가 거부되었습니다. 원격 변경을 먼저 가져와 합친 뒤에 다시 push하면 됩니다.

```
! [rejected] main -> main (non-fast-forward)
```

1. 원격 변경을 가져옵니다.
   ```
   git fetch origin
   ```
2. 내 커밋을 원격 `main` 위로 옮깁니다.
   ```
   git pull --rebase origin main
   ```
3. 충돌이 나면 파일을 고치고 `git add <파일>`을 실행한 뒤 `git rebase --continue`를 실행합니다.
4. 다시 push합니다.
   ```
   git push origin main
   ```

rebase 대신 merge 커밋을 남기려면 2단계에서 `git pull origin main`을 실행합니다.

`git push --force`는 쓰지 마십시오. 원격에 있는 다른 사람의 커밋이 사라집니다.
