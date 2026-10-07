`venv` 모듈로 가상환경을 만들고, 운영체제에 맞는 스크립트로 활성화합니다.

1. 프로젝트 폴더에서 가상환경을 만듭니다.

   ```bash
   python3 -m venv .venv
   ```

2. 가상환경을 활성화합니다.

   | 환경 | 명령 |
   |---|---|
   | Linux, macOS, WSL (bash, zsh) | `source .venv/bin/activate` |
   | Windows PowerShell | `.venv\Scripts\Activate.ps1` |
   | Windows cmd | `.venv\Scripts\activate.bat` |

3. 활성화되면 프롬프트 앞에 `(.venv)`가 표시됩니다. `which python`으로 경로가 `.venv` 안인지 확인합니다.

4. 패키지는 활성화한 상태에서 설치합니다.

   ```bash
   pip install requests
   ```

5. 작업이 끝나면 비활성화합니다.

   ```bash
   deactivate
   ```

PowerShell에서 실행 정책 오류가 나면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 실행합니다. 이 명령은 현재 사용자의 스크립트 실행 권한을 바꿉니다.

`.venv` 폴더는 Git에 올리지 않습니다. `.gitignore`에 `.venv/`를 추가합니다.
