원인은 pip가 `foo`라는 패키지의 배포 파일을 하나도 찾지 못한 것입니다. `from versions: none`은 9.9만 없다는 뜻이 아니라 어떤 버전도 보이지 않는다는 뜻입니다.

아직 사용자 환경을 확인하지 않았으므로 아래는 가능성이 높은 순서의 후보입니다.

| 후보 | 설명 |
|---|---|
| 패키지 이름 오류 | 철자가 틀렸거나 PyPI에 없는 이름입니다. |
| 인덱스 접속 실패 | 오프라인, 프록시, 방화벽 문제로 PyPI에 닿지 못합니다. |
| 인덱스 설정 오류 | `pip.conf`, `PIP_INDEX_URL`, `--index-url`이 엉뚱한 주소를 가리킵니다. |
| Python 버전 불일치 | 현재 Python이 지원 범위 밖이라 모든 파일이 걸러집니다. |
| pip 또는 Python이 너무 오래됨 | 최신 TLS나 메타데이터를 처리하지 못합니다. |

확인 절차는 다음과 같습니다.

1. `pip index versions foo`로 패키지가 인덱스에 있는지 확인합니다.
2. `pip config list`로 인덱스 설정을 확인합니다.
3. `env | grep -i -E 'pip|proxy'`로 환경 변수를 확인합니다.
4. `python --version`과 `pip --version`을 확인합니다.
5. `pip install -v foo==9.9`로 pip가 어느 주소를 조회하는지 확인합니다.

`foo`가 사설 패키지라면 사내 인덱스 주소를 `--index-url` 또는 `--extra-index-url`로 지정해야 합니다.

5번 명령의 출력이나 `pip config list` 결과를 붙여 주면 원인을 좁혀 드리겠습니다.
