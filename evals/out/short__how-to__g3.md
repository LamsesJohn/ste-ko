`venv` 모듈로 가상환경을 만들고 OS에 맞는 스크립트로 활성화합니다.

1. 가상환경을 만듭니다.
   ```bash
   python3 -m venv .venv
   ```
2. 가상환경을 활성화합니다.
   - Linux, macOS, WSL (bash, zsh)
     ```bash
     source .venv/bin/activate
     ```
   - Windows PowerShell
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - Windows cmd
     ```cmd
     .venv\Scripts\activate.bat
     ```
3. 프롬프트 앞에 `(.venv)`가 보이면 활성화된 상태입니다.
4. 패키지를 설치합니다.
   ```bash
   pip install requests
   ```
5. 작업이 끝나면 비활성화합니다.
   ```bash
   deactivate
   ```

참고 사항은 다음과 같습니다.

| 항목 | 설명 |
|---|---|
| 폴더 이름 | `.venv`가 일반적이며 다른 이름도 가능합니다 |
| 의존성 저장 | `pip freeze > requirements.txt` |
| 의존성 복원 | `pip install -r requirements.txt` |
| Git 제외 | `.gitignore`에 `.venv/`를 추가합니다 |

현재 환경은 WSL(bash)이므로 `source .venv/bin/activate`를 쓰면 됩니다. 이 환경에서 직접 실행해 검증하지는 않았습니다.

`venv` 생성 시 `ensurepip is not available` 오류가 나면 `sudo apt install python3-venv`로 패키지를 설치합니다.
