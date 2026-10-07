원격 `main`에 내 로컬에 없는 커밋이 있어서 거부된 거예요. 먼저 원격 변경을 가져와서 합친 뒤 push하면 됩니다.

**1. 원격 변경 확인**
```bash
git fetch origin
git log HEAD..origin/main --oneline   # 원격에만 있는 커밋
```

**2. 합치기 (둘 중 하나)**

- merge 방식 (히스토리 그대로 보존, 가장 안전):
  ```bash
  git pull origin main
  ```
- rebase 방식 (히스토리를 일직선으로 유지):
  ```bash
  git pull --rebase origin main
  ```

**3. 충돌이 나면**
충돌 파일을 수정한 뒤:
```bash
git add <파일>
git merge --continue      # rebase였다면: git rebase --continue
```

**4. push**
```bash
git push origin main
```

**주의:** `git push --force`는 쓰지 마세요. 원격에 있는 다른 사람의 커밋을 덮어써서 날려버릴 수 있습니다. 정말 필요한 상황(예: 본인이 rebase로 히스토리를 고쳐 쓴 경우)이라면 `git push --force-with-lease`가 그나마 안전합니다.

참고로 현재 작업 디렉터리(`/tmp/tmp6vzdzrit`)는 git 저장소가 아니라서, 해당 명령은 실제 프로젝트 폴더에서 실행하셔야 해요. 충돌이 나거나 결과가 이상하면 출력 내용을 붙여 주시면 같이 봐드릴게요.
