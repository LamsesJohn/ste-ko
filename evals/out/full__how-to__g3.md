`python3 -m venv`로 가상환경을 만들고, 운영체제에 맞는 `activate` 스크립트로 활성화합니다.

## 만들기

1. 프로젝트 폴더로 이동합니다.
2. 아래 명령을 실행합니다.

```bash
python3 -m venv .venv
```

이 명령은 현재 폴더에 `.venv` 폴더를 만듭니다. 폴더 이름은 바꿔도 됩니다.

## 활성화

| 환경 | 명령 |
|---|---|
| Linux, macOS, WSL (bash, zsh) | `source .venv/bin/activate` |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows cmd | `.venv\Scripts\activate.bat` |

활성화하면 프롬프트 앞에 `(.venv)`가 붙습니다.

## 확인

```bash
which python
```

출력 경로가 `.venv/bin/python`으로 끝나면 활성화된 상태입니다.

## 사용과 종료

- 활성화한 상태에서 `pip install 패키지명`을 실행하면 패키지가 `.venv` 안에만 설치됩니다.
- 비활성화하려면 `deactivate`를 실행합니다.

## 주의

- PowerShell에서 실행 정책 오류가 나면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 실행합니다. 이 명령은 현재 사용자의 스크립트 실행 정책을 바꿉니다.
- Debian과 Ubuntu에서 `ensurepip is not available` 오류가 나면 `sudo apt install python3-venv`를 실행합니다.
- `.venv`는 git에 올리지 않습니다. `.gitignore`에 `.venv/`를 추가합니다.
