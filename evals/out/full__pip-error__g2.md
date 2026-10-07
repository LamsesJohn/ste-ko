`foo`의 설치 가능한 파일을 pip가 하나도 찾지 못했다는 뜻입니다. 사용자의 환경은 아직 확인하지 못했으므로 아래는 가능한 원인입니다.

사용자가 붙여 넣은 오류는 다음과 같습니다.

```
ERROR: Could not find a version that satisfies the requirement foo==9.9 (from versions: none)
```

## 원인 후보

1. 패키지 이름이 틀렸거나 해당 인덱스에 없습니다.
2. 네트워크, 프록시, 방화벽이 인덱스 접속을 막습니다.
3. `pip.conf`나 `--index-url`이 다른 인덱스를 가리킵니다. 그 인덱스에 `foo`가 없을 수 있습니다.
4. 현재 Python 버전이나 플랫폼에 맞는 파일이 없습니다. 이 경우에도 `from versions: none`이 나올 수 있습니다.
5. pip 버전이 오래되었습니다.

## 확인 순서

1. 인덱스 설정을 확인합니다.

   ```
   pip config list
   ```

2. Python과 pip 버전을 확인합니다.

   ```
   python --version
   pip --version
   ```

3. 버전을 지정하지 않고 사용 가능한 버전을 조회합니다.

   ```
   pip index versions foo
   ```

4. 접속 문제가 의심되면 자세한 로그를 확인합니다.

   ```
   pip install foo==9.9 -v
   ```

`pip config list`와 `pip install foo==9.9 -v`의 출력을 붙여 넣으면 원인을 좁힐 수 있습니다.
