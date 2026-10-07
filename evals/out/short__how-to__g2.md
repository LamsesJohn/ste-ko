`venv` 모듈로 가상환경을 만들고 운영체제에 맞는 스크립트로 활성화합니다.

1. 프로젝트 폴더로 이동합니다.
2. 가상환경을 만듭니다.

```bash
python3 -m venv .venv
```

3. 가상환경을 활성화합니다.

| 환경 | 명령어 |
|---|---|
| Linux, macOS, WSL (bash, zsh) | `source .venv/bin/activate` |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows cmd | `.venv\Scripts\activate.bat` |

4. 활성화되면 프롬프트 앞에 `(.venv)`가 표시됩니다.
5. 패키지를 설치합니다.

```bash
pip install requests
```

6. 작업을 마치면 비활성화합니다.

```bash
deactivate
```

참고 사항은 다음과 같습니다.

- 현재 환경은 WSL이므로 `source .venv/bin/activate`를 사용합니다.
- Git을 쓰는 프로젝트라면 `.gitignore`에 `.venv/`를 추가합니다.
- 설치한 패키지 목록은 `pip freeze > requirements.txt`로 저장합니다.
- 다른 환경에서는 `pip install -r requirements.txt`로 같은 패키지를 설치합니다.
- Debian 계열에서 `venv` 생성이 실패하면 `sudo apt install python3-venv`를 먼저 실행합니다.

이 환경에서 직접 실행해 확인하지는 않았습니다. 위 내용은 표준 `venv` 동작에 근거합니다.
