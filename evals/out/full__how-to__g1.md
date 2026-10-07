내장 모듈 `venv`로 가상환경을 만들고 활성화합니다.

1. 가상환경을 만듭니다.

   ```bash
   python3 -m venv .venv
   ```

2. 가상환경을 활성화합니다. 운영체제와 셸에 따라 명령이 다릅니다.

   | 환경 | 명령 |
   |---|---|
   | Linux, macOS, WSL (bash, zsh) | `source .venv/bin/activate` |
   | Windows PowerShell | `.venv\Scripts\Activate.ps1` |
   | Windows cmd | `.venv\Scripts\activate.bat` |

3. 활성화되었는지 확인합니다. 프롬프트 앞에 `(.venv)`가 표시됩니다.

   ```bash
   which python
   ```

   출력 경로가 `.venv/bin/python`으로 끝나면 활성화된 것입니다.

4. 패키지를 설치합니다. 패키지는 `.venv` 안에만 설치됩니다.

   ```bash
   pip install requests
   ```

5. 작업이 끝나면 가상환경을 비활성화합니다.

   ```bash
   deactivate
   ```

PowerShell에서 스크립트 실행이 막히면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 실행합니다.

`.venv` 폴더는 Git에 올리지 않습니다. `.gitignore`에 `.venv/`를 추가합니다.
