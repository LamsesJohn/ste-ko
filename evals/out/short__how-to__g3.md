`venv` 모듈로 가상환경을 만들고 활성화 스크립트를 실행하면 됩니다.

1. 가상환경을 만듭니다.
   ```bash
   python3 -m venv .venv
   ```

2. 가상환경을 활성화합니다.

| 환경 | 명령어 |
|---|---|
| Linux, macOS, WSL (bash, zsh) | `source .venv/bin/activate` |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows cmd | `.venv\Scripts\activate.bat` |

3. 활성화되면 프롬프트 앞에 `(.venv)`가 표시됩니다.

4. 패키지를 설치합니다.
   ```bash
   pip install requests
   ```

5. 작업을 마치면 비활성화합니다.
   ```bash
   deactivate
   ```

참고 사항입니다.

- 가상환경 폴더 이름은 `.venv`가 관례입니다. 다른 이름도 쓸 수 있습니다.
- Git을 쓴다면 `.venv/`를 `.gitignore`에 추가하세요.
- PowerShell에서 스크립트 실행이 막히면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 실행하세요.
- Debian 계열 Linux에서 `venv`가 없다고 나오면 `sudo apt install python3-venv`를 실행하세요.

이 내용은 표준 `venv` 기준이며, 현재 환경에서 직접 실행해 확인하지는 않았습니다.
