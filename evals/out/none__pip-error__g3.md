`from versions: none`은 pip이 해당 패키지의 **어떤 버전도 찾지 못했다**는 뜻이에요. 9.9 버전이 없다는 것과는 다릅니다(그 경우엔 사용 가능한 버전 목록이 나와요). 주요 원인은 다음과 같습니다.

1. **패키지 이름 오타 또는 존재하지 않는 패키지**: PyPI에 `foo`가 없거나 이름이 다를 수 있어요. `pip index versions foo` 또는 pypi.org에서 확인해 보세요.
2. **네트워크/프록시 문제**: 회사망, 방화벽, 프록시, WSL의 DNS 문제 등으로 PyPI에 접속하지 못하는 경우. 위쪽에 `Retrying...`, `SSL`, `connection` 관련 경고가 있었는지 확인해 보세요.
3. **Python 버전/플랫폼 불일치**: 패키지가 현재 Python 버전(`Requires-Python`)이나 OS/아키텍처용 배포 파일을 제공하지 않으면 후보가 모두 걸러져 `none`이 됩니다. `python --version`을 확인하세요.
4. **오래된 pip**: `python -m pip install --upgrade pip` 후 재시도해 보세요.
5. **사설/다른 인덱스 설정**: `pip config list`, `PIP_INDEX_URL`, `pip.conf`에 `index-url`이 사설 저장소로 지정되어 있으면 거기에 패키지가 없을 수 있어요.
6. **버전 자체가 없는 경우**: 보통은 `(from versions: 1.0, 1.1, ...)`처럼 목록이 나오지만, 모든 릴리스가 yank(철회)되었거나 pre-release만 있는 경우에도 `none`이 나올 수 있어요 (이때는 `--pre` 필요).

빠른 진단 명령:
```bash
python --version
pip --version
pip config list
pip index versions foo
pip install foo==9.9 -v
```

마지막 `-v` 출력과 실제 패키지 이름, Python 버전을 알려주시면 원인을 더 좁혀 드릴게요.
