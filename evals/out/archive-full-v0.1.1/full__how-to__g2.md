`venv` 모듈로 가상환경을 만들고 `activate` 스크립트로 활성화한다.

1. 프로젝트 폴더에서 가상환경을 만든다.

   ```bash
   python3 -m venv .venv
   ```

2. 가상환경을 활성화한다.

   | 환경 | 명령 |
   |---|---|
   | Linux, macOS, WSL (bash, zsh) | `source .venv/bin/activate` |
   | Windows PowerShell | `.venv\Scripts\Activate.ps1` |
   | Windows cmd | `.venv\Scripts\activate.bat` |

3. 프롬프트 앞에 `(.venv)`가 보이면 활성화된 것이다.

4. 패키지를 설치한다. 이 패키지는 `.venv` 안에만 설치된다.

   ```bash
   pip install requests
   ```

5. 작업을 마치면 비활성화한다.

   ```bash
   deactivate
   ```

PowerShell에서 스크립트 실행이 막히면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 실행한다.

`.venv` 폴더는 Git에 올리지 않는다. `.gitignore`에 `.venv/`를 추가한다. 의존성은 `pip freeze > requirements.txt`로 기록한다.
