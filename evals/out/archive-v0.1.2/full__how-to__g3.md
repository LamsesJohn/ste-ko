`venv` 모듈로 가상환경을 만들고, 운영체제에 맞는 스크립트로 활성화합니다.

1. 프로젝트 폴더에서 가상환경을 만듭니다.

   ```bash
   python3 -m venv .venv
   ```

   Windows에서는 `python -m venv .venv`를 씁니다.

2. 가상환경을 활성화합니다.

   | 환경 | 명령 |
   |---|---|
   | Linux, macOS (bash, zsh) | `source .venv/bin/activate` |
   | Windows PowerShell | `.venv\Scripts\Activate.ps1` |
   | Windows cmd | `.venv\Scripts\activate.bat` |

   활성화하면 프롬프트 앞에 `(.venv)`가 붙습니다.

3. 패키지를 설치합니다. 패키지는 `.venv` 안에만 설치됩니다.

   ```bash
   pip install requests
   ```

4. 작업을 마치면 비활성화합니다.

   ```bash
   deactivate
   ```

PowerShell에서 실행 정책 오류가 나면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 실행합니다. 이 명령은 현재 사용자의 스크립트 실행 정책을 바꿉니다.

Linux에서 `venv`를 찾지 못하면 `sudo apt install python3-venv`로 설치합니다. Debian과 Ubuntu 계열에서 이 오류가 자주 나옵니다.

`.venv` 폴더는 Git에 올리지 않습니다. `.gitignore`에 `.venv/`를 추가합니다.
