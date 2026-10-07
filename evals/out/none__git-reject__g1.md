원격 `main`에 내 로컬에 없는 커밋이 있어서 거부된 거예요. 먼저 원격 변경을 가져와 합친 뒤 push 하면 됩니다.

**1. 원격 변경 확인**
```bash
git fetch origin
git log --oneline HEAD..origin/main   # 원격에만 있는 커밋
```

**2. 합치기 (둘 중 하나 선택)**

- **rebase (히스토리를 일직선으로 유지, 추천)**
  ```bash
  git pull --rebase origin main
  ```
- **merge (머지 커밋 생성)**
  ```bash
  git pull origin main
  ```

충돌이 나면 파일을 수정한 뒤:
```bash
git add <파일>
git rebase --continue   # merge 방식이면 git commit
```

**3. push**
```bash
git push origin main
```

**주의:** `git push --force`는 원격의 다른 사람 커밋을 지워버릴 수 있으니, 원격 내용을 버려도 확실히 괜찮은 경우가 아니면 쓰지 마세요. 꼭 써야 한다면 `--force-with-lease`가 더 안전합니다.

참고로 지금 작업 디렉터리(`/tmp/tmp6vzdzrit`)는 git 저장소가 아니라서, 실제 저장소 디렉터리에서 실행해야 해요. 충돌이 나거나 출력이 이해되지 않으면 결과를 붙여 주세요, 같이 봐드릴게요.
