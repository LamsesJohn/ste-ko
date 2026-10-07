내장 모듈 `venv`로 가상환경을 만들고 활성화한다.

## 만들기

프로젝트 폴더에서 아래 명령을 실행한다.

```bash
python3 -m venv .venv
```

`.venv` 폴더가 생긴다. 폴더 이름은 바꿔도 된다.

## 활성화

운영체제와 셸에 맞는 명령을 실행한다.

| 환경 | 명령 |
|---|---|
| Linux, macOS, WSL (bash, zsh) | `source .venv/bin/activate` |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows cmd | `.venv\Scripts\activate.bat` |

활성화하면 프롬프트 앞에 `(.venv)`가 붙는다.

## 확인

```bash
which python
```

출력 경로에 `.venv`가 있으면 활성화된 것이다.

## 패키지 설치

```bash
pip install requests
```

이 패키지는 `.venv` 안에만 설치된다.

## 비활성화

```bash
deactivate
```

## 참고

- PowerShell에서 실행 정책 오류가 나면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 실행한다. 이 명령은 현재 사용자의 스크립트 실행 정책을 바꾼다.
- Git을 쓰면 `.gitignore`에 `.venv/`를 추가한다. 가상환경 폴더는 저장소에 올리지 않는다.
- Linux에서 `venv` 모듈이 없다는 오류가 나면 `sudo apt install python3-venv`를 실행한다.
