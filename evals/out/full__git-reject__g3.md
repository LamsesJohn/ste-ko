`! [rejected] main -> main (non-fast-forward)`는 원격 `main`에 내 로컬에 없는 커밋이 있다는 뜻입니다. 먼저 원격 변경을 가져와 합친 뒤 다시 push해야 합니다.

1. 원격 변경을 가져와 내 커밋 위에 다시 쌓습니다.

   ```
   git pull --rebase origin main
   ```

2. 충돌이 나면 파일을 고치고 아래 명령을 실행합니다. 충돌이 없을 때까지 반복합니다.

   ```
   git add <파일>
   git rebase --continue
   ```

3. push합니다.

   ```
   git push origin main
   ```

merge 커밋을 남기고 싶으면 1번에서 `git pull origin main`을 씁니다.

`git push --force`는 쓰지 않습니다. 원격에 있는 다른 사람의 커밋이 사라집니다. 내 로컬 기록으로 원격을 덮어쓰는 것이 의도라면 `git push --force-with-lease`를 쓰고, 그 전에 `git log origin/main`으로 지워질 커밋을 확인합니다.

이 디렉터리는 git 저장소가 아니어서 상태를 직접 확인하지 못했습니다. 위 명령은 push를 실행한 저장소에서 실행합니다.
