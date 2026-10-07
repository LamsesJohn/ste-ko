`from versions: none`은 pip이 해당 패키지의 **어떤 버전도 찾지 못했다**는 뜻이에요. 9.9라는 버전만 없는 게 아니라, 설치 가능한 후보가 아예 0개라는 의미입니다. 주요 원인은 다음과 같습니다.

**1. 패키지 이름 오타 또는 존재하지 않는 패키지**
- PyPI에 `foo`가 없거나 이름이 다를 수 있어요. https://pypi.org/project/foo/ 에서 확인해 보세요.
- 확인: `pip index versions foo` 또는 `pip download foo --no-deps`

**2. Python 버전/플랫폼이 맞지 않음**
- 패키지가 `Requires-Python`으로 현재 Python 버전을 지원하지 않거나, 현재 OS/아키텍처용 wheel이 없고 sdist도 없는 경우입니다.
- 확인: `python --version`, `pip --version` (pip이 다른 Python에 묶여 있을 수도 있음 → `python -m pip install ...` 사용 권장)
- 이 경우 보통 `(from versions: none)`이 나오고, `-v`를 붙이면 "Skipping link ... requires a different Python" 같은 메시지가 보입니다.

**3. 네트워크/프록시/미러 문제**
- 사내 프록시, 방화벽, VPN, 또는 WSL 네트워크 문제로 PyPI에 접근 못 하는 경우.
- 확인: `pip config list`, `pip install foo -v`, `curl -I https://pypi.org/simple/foo/`
- `index-url`이 사설 저장소나 오래된 미러로 설정돼 있으면 거기에 패키지가 없을 수 있어요 (`~/.config/pip/pip.conf`, `PIP_INDEX_URL` 환경변수 확인).

**4. 너무 오래된 pip**
- 오래된 pip은 최신 메타데이터나 wheel 태그를 인식하지 못합니다. `python -m pip install --upgrade pip`

**5. 사전 릴리스/yanked 버전만 존재**
- 버전이 전부 yanked이거나 pre-release뿐이면 안 보일 수 있어요. pre-release는 `--pre` 옵션이 필요합니다.

**빠른 진단 순서**
```bash
python -m pip install --upgrade pip
python -m pip install foo==9.9 -v
pip config list
```
`-v` 출력에서 어떤 URL에 접근하는지, 어떤 링크를 왜 건너뛰는지 보면 원인이 거의 바로 드러나요.

실제 패키지 이름과 `-v` 출력을 알려주시면 더 정확히 짚어드릴 수 있습니다.
