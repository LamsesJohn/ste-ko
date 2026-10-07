`from versions: none`은 pip이 해당 패키지의 **버전을 하나도 찾지 못했다**는 뜻이에요. 특정 버전(9.9)만 없는 경우라면 보통 `from versions: 1.0, 1.1, ...`처럼 목록이 나오거든요. 주요 원인은 다음과 같아요.

1. **패키지 이름 오타 / 존재하지 않는 패키지**
   `pip index versions foo` 또는 https://pypi.org/project/foo/ 에서 확인해 보세요.

2. **Python 버전 불일치**
   패키지가 지원하는 Python 버전(`Requires-Python`)이 현재 인터프리터와 맞지 않으면 모든 릴리스가 걸러져서 `none`이 됩니다. `python --version`과 PyPI 페이지의 요구 버전을 비교해 보세요.

3. **플랫폼/아키텍처에 맞는 wheel이 없음**
   소스 배포(sdist)도 없고 내 OS/CPU(예: ARM, 최신 Python)용 wheel만 없는 경우예요.

4. **네트워크 문제**
   프록시, 방화벽, 회사 사내망, WSL의 DNS 문제 등으로 인덱스에 접근하지 못할 때도 이렇게 나옵니다. 위에 `Retrying...`, `SSL`, `connection` 관련 경고가 같이 떴는지 확인해 보세요.

5. **인덱스 설정 문제**
   `pip.conf`, `PIP_INDEX_URL`, `--index-url`/`--extra-index-url`이 비공개 저장소나 잘못된 주소를 가리키고 있을 수 있어요. `pip config list`로 확인해 보세요.

6. **오래된 pip**
   `python -m pip install --upgrade pip` 후 재시도해 보세요.

**빠른 진단 순서**
```bash
python --version
pip --version
pip config list
pip download foo -v        # 어떤 URL에 접속하고 어떤 파일을 걸러내는지 상세히 보여줌
pip install foo -v         # 버전 지정 없이 시도
```

`-v` 출력에서 "Skipping link ... requires a different Python" 같은 메시지가 보이면 2번, 연결 오류가 보이면 4번이에요. 실제 패키지 이름과 `pip install -v` 출력을 알려주시면 더 정확히 짚어드릴게요.
