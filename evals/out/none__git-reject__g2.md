원격 `main`에 내 로컬에 없는 커밋이 있어서 거부된 거예요. 먼저 원격 변경을 가져와 합친 뒤 push하면 됩니다.

**1. 원격 상태 확인**
```bash
git fetch origin
git log --oneline HEAD..origin/main   # 원격에만 있는 커밋
```

**2. 통합 (둘 중 하나 선택)**

- 머지 방식 (기록 그대로 보존, 가장 안전):
  ```bash
  git pull origin main
  ```
- 리베이스 방식 (히스토리가 한 줄로 깔끔):
  ```bash
  git pull --rebase origin main
  ```

충돌이 나면 파일을 수정한 뒤:
```bash
git add <파일>
git merge --continue     # 리베이스였다면: git rebase --continue
```

**3. push**
```bash
git push origin main
```

**주의:** `git push --force`는 쓰지 마세요. 원격의 다른 사람 커밋을 덮어써서 날려버릴 수 있습니다. 내가 커밋을 amend/rebase해서 일부러 히스토리를 고쳐 쓴 경우에만, 팀과 확인한 뒤 `git push --force-with-lease`를 쓰세요.

참고로 현재 작업 디렉터리(`/tmp/tmp6vzdzrit`)는 git 저장소가 아니라서, 해당 명령은 실제 프로젝트 폴더에서 실행해야 해요. 실행 후 충돌이 나거나 이상한 출력이 나오면 알려주세요.
