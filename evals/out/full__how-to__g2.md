`python3 -m venv`로 가상환경을 만들고 `activate` 스크립트로 활성화합니다.

1. 프로젝트 폴더로 이동합니다.
2. 가상환경을 만듭니다.

   ```bash
   python3 -m venv .venv
   ```

3. 가상환경을 활성화합니다.

   - Linux, macOS, WSL (bash, zsh):

     ```bash
     source .venv/bin/activate
     ```

   - Windows PowerShell:

     ```powershell
     .venv\Scripts\Activate.ps1
     ```

   - Windows cmd:

     ```bat
     .venv\Scripts\activate.bat
     ```

4. 활성화되면 프롬프트 앞에 `(.venv)`가 표시됩니다.
5. 패키지를 설치합니다. 이 패키지는 `.venv` 안에만 설치됩니다.

   ```bash
   pip install requests
   ```

6. 작업이 끝나면 비활성화합니다.

   ```bash
   deactivate
   ```

`python3 -m venv`가 실패하면 Debian과 Ubuntu에서는 `sudo apt install python3-venv`로 `venv` 모듈을 설치합니다.

`.venv` 폴더는 git에 올리지 않습니다. `.gitignore`에 `.venv/`를 추가합니다. 다른 환경에서는 `pip freeze > requirements.txt`로 만든 파일을 `pip install -r requirements.txt`로 설치해 같은 환경을 만듭니다.
