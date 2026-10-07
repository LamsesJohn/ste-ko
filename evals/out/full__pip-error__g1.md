`from versions: none`은 pip이 `foo`라는 이름으로 설치할 수 있는 파일을 하나도 찾지 못했다는 뜻입니다. `9.9`만 없는 것이 아니라 어떤 버전도 보이지 않습니다. 현재 환경은 확인하지 못해서 원인은 아래 후보 중 하나로 추정합니다.

## 원인 후보

1. 패키지 이름이 틀렸거나 PyPI에 없습니다.
2. 네트워크, 프록시, 방화벽이 인덱스 접속을 막습니다.
3. `pip.conf`나 `--index-url`이 접근할 수 없는 사설 인덱스를 가리킵니다.
4. 현재 Python 버전이나 플랫폼에 맞는 배포 파일이 없습니다. 패키지의 `Requires-Python` 조건이 맞지 않을 때도 이렇게 보입니다.
5. pip이 너무 오래되어 최신 인덱스 형식을 처리하지 못합니다.

## 확인 순서

1. 이름을 확인합니다. 브라우저에서 `https://pypi.org/project/foo/`를 엽니다.
2. Python과 pip 버전을 확인합니다.

   ```
   python --version
   python -m pip --version
   ```

3. pip이 보는 버전 목록을 확인합니다.

   ```
   python -m pip index versions foo
   ```

4. 인덱스 설정을 확인합니다.

   ```
   python -m pip config list
   ```

5. 자세한 로그를 봅니다. 접속 실패나 `Requires-Python` 불일치 메시지가 나옵니다.

   ```
   python -m pip install foo==9.9 -v
   ```

6. pip을 갱신한 뒤 다시 시도합니다.

   ```
   python -m pip install --upgrade pip
   ```

3번과 5번의 출력을 붙여 주시면 원인을 좁힐 수 있습니다.
