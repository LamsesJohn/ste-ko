내장 모듈 `venv`로 가상환경을 만들고, 활성화 스크립트를 실행합니다.

1. 프로젝트 폴더로 이동합니다.
2. 가상환경을 만듭니다.

   ```bash
   python3 -m venv .venv
   ```

3. 가상환경을 활성화합니다.

   | 환경 | 명령 |
   |---|---|
   | Linux, macOS (bash, zsh) | `source .venv/bin/activate` |
   | Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
   | Windows (cmd) | `.venv\Scripts\activate.bat` |

4. 활성화되면 프롬프트 앞에 `(.venv)`가 붙습니다.
5. 패키지를 설치합니다.

   ```bash
   pip install requests
   ```

6. 작업이 끝나면 비활성화합니다.

   ```bash
   deactivate
   ```

PowerShell에서 "스크립트 실행이 비활성화되어 있습니다"라는 오류가 나면, 아래 명령으로 현재 사용자의 실행 정책을 바꿉니다. 이 명령은 시스템 설정을 바꾸므로 정책을 이해한 뒤에 실행하십시오.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

`.venv` 폴더는 Git에 올리지 않습니다. `.gitignore`에 `.venv/`를 추가하십시오.
