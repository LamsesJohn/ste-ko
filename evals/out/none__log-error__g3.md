`Connection refused`는 해당 주소와 포트에서 아무 프로세스도 연결을 받지 않는다는 뜻입니다. 정확한 원인을 찾기 위해 프로젝트에서 테스트가 어디에 접속하는지 먼저 확인해 보겠습니다.


<invoke name="Grep">
<parameter name="pattern">localhost|127\.0\.0\.1|connect\(|create_connection|requests\.|redis|psycopg|PORT</parameter>
<parameter name="path">/tmp/tmp1nzl0htd</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
<parameter name="head_limit">50</parameter>
</invoke>
<invoke name="Glob">
<parameter name="pattern">**/{docker-compose*.y*ml,Dockerfile,conftest.py,pytest.ini,tox.ini,.env*,Makefile}</parameter>
<parameter name="path">/tmp/tmp1nzl0htd</parameter>
</invoke>
