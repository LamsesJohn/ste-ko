테스트가 접속하려는 호스트와 포트에서 아무 프로세스도 연결을 받지 않아서 `ConnectionRefusedError: [Errno 111] Connection refused`가 발생했습니다. 아직 코드를 보지 못해서 어떤 서비스인지는 확인하지 못했습니다. 테스트가 접속하는 주소를 먼저 찾아보겠습니다.


<invoke name="Grep">
<parameter name="pattern">localhost|127\.0\.0\.1|0\.0\.0\.0|connect\(|create_connection|redis|postgres|PORT</parameter>
<parameter name="path">/tmp/tmp6vzdzrit</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
<parameter name="head_limit">50</parameter>
</invoke>
<invoke name="Glob">
<parameter name="pattern">**/{docker-compose*.y*ml,conftest.py,.env*,pytest.ini,pyproject.toml,Makefile}</parameter>
<parameter name="path">/tmp/tmp6vzdzrit</parameter>
</invoke>
