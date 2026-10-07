## 가상환경 만들기 (venv)

```bash
python3 -m venv .venv
```

`.venv`는 폴더 이름이며, 원하는 이름으로 바꿔도 됩니다.

## 활성화

**Linux / macOS / WSL (bash, zsh)**
```bash
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (cmd)**
```cmd
.venv\Scripts\activate.bat
```

활성화되면 프롬프트 앞에 `(.venv)`가 표시됩니다.

## 사용

```bash
pip install requests          # 패키지 설치
pip freeze > requirements.txt # 의존성 저장
pip install -r requirements.txt  # 저장한 의존성 설치
```

## 비활성화

```bash
deactivate
```

## 참고

- **Debian/Ubuntu(WSL 포함)**에서 `ensurepip` 오류가 나면 먼저 다음을 설치하세요:
  ```bash
  sudo apt install python3-venv
  ```
- PowerShell에서 스크립트 실행이 막혀 있으면:
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```
- Git을 쓴다면 `.gitignore`에 `.venv/`를 추가하세요.
- 더 빠른 대안으로 `uv`도 있습니다: `uv venv` 후 `source .venv/bin/activate`, 패키지는 `uv pip install ...`로 설치합니다.
