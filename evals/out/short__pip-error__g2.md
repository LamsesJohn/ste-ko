**pip이 `foo`라는 패키지 파일을 하나도 찾지 못했다는 뜻입니다.** 버전 9.9만 없는 것이 아니라 `(from versions: none)`은 어떤 버전도 보이지 않는다는 의미입니다.

저는 사용자의 환경을 직접 확인하지 못했습니다. 아래는 이 오류 문구에서 흔한 원인입니다.

| 원인 | 확인 방법 |
|---|---|
| 패키지 이름 오타 또는 존재하지 않는 이름 | `pip index versions foo` 또는 pypi.org에서 검색 |
| 네트워크, 프록시, 방화벽 차단 | `pip install foo -v`로 연결 오류 확인 |
| 잘못된 인덱스 설정 | `pip config list`로 `index-url` 확인 |
| 사내 미러에 해당 패키지 없음 | 미러 주소를 `--index-url https://pypi.org/simple`로 바꿔 시도 |
| 너무 오래된 Python 또는 pip | `python --version`, `pip --version` 확인 |
| 현재 플랫폼용 배포 파일이 없음 | 패키지 페이지의 Download files 목록 확인 |

다음 순서로 진단하는 것을 권합니다.

1. `pip install foo -v`를 실행하고 출력에서 `Looking in indexes:` 줄을 확인합니다.
2. 그 줄의 주소가 의도한 인덱스인지 확인합니다.
3. `pip config list`와 환경 변수 `PIP_INDEX_URL`, `HTTP_PROXY`, `HTTPS_PROXY`를 점검합니다.
4. `python -m pip install --upgrade pip`로 pip을 업데이트합니다.
5. 이름이 맞다면 `pip install foo --index-url https://pypi.org/simple`로 다시 시도합니다.

`foo`는 예시 이름일 수 있습니다. 실제 패키지 이름과 `-v` 출력을 보여 주시면 원인을 좁혀 드리겠습니다.
