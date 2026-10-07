`venv` 모듈로 가상환경을 만들고 운영체제에 맞는 스크립트로 활성화합니다.

1. 프로젝트 폴더로 이동합니다.
2. 가상환경을 만듭니다.

```bash
python3 -m venv .venv
```

3. 가상환경을 활성화합니다.

| 환경 | 명령 |
|---|---|
| Linux, macOS, WSL (bash, zsh) | `source .venv/bin/activate` |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows cmd | `.venv\Scripts\activate.bat` |

4. 활성화되면 프롬프트 앞에 `(.venv)`가 표시됩니다.
5. 패키지를 설치합니다.

```bash
pip install requests
```

6. 작업이 끝나면 비활성화합니다.

```bash
deactivate
```

참고 사항은 다음과 같습니다.

- 현재 환경은 WSL bash이므로 `source .venv/bin/activate`를 쓰면 됩니다.
- 일부 Linux 배포판에서는 `python3-venv` 패키지가 따로 필요합니다. 설치 명령은 `sudo apt install python3-venv`입니다.
- PowerShell에서 실행 정책 오류가 나면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 실행합니다.
- `.venv` 폴더는 Git에 올리지 않도록 `.gitignore`에 추가합니다.
- 의존성 목록은 `pip freeze > requirements.txt`로 저장하고 `pip install -r requirements.txt`로 복원합니다.

이 답변은 `venv` 표준 동작에 근거하며, 이 환경에서 직접 실행해 확인하지는 않았습니다.
