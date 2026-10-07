# Python 가상환경 만들기와 활성화

## 1. 생성 (`venv` 사용)

```bash
python3 -m venv .venv
```

`.venv`는 폴더 이름이며, 원하는 이름으로 바꿔도 됩니다.

## 2. 활성화

**Linux / macOS / WSL (bash, zsh):**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (cmd):**
```cmd
.venv\Scripts\activate.bat
```

활성화되면 프롬프트 앞에 `(.venv)`가 표시됩니다.

## 3. 사용

```bash
pip install requests          # 패키지 설치
pip freeze > requirements.txt # 의존성 저장
pip install -r requirements.txt  # 저장된 의존성 설치
```

## 4. 비활성화

```bash
deactivate
```

## 참고

- **WSL/Ubuntu**에서 `venv` 모듈이 없다는 오류가 나면:
  ```bash
  sudo apt install python3-venv
  ```
- **PowerShell**에서 스크립트 실행이 차단되면:
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```
- `.venv`는 git에 커밋하지 않도록 `.gitignore`에 추가하세요.
- 더 빠른 대안으로 `uv`도 있습니다:
  ```bash
  uv venv
  source .venv/bin/activate
  uv pip install requests
  ```

현재 환경이 WSL(bash)이므로 위의 Linux 방식이 그대로 적용됩니다. 원하시면 이 디렉터리에 직접 만들어 드릴 수도 있습니다.
