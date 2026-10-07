원인은 테스트가 접속하려는 호스트와 포트에서 아무 프로세스도 듣고 있지 않다는 것입니다. 아직 코드를 확인하지 못했으므로 접속 대상을 찾아보겠습니다.


<invoke name="Grep">
<parameter name="pattern">localhost|127\.0\.0\.1|connect\(|create_connection|requests\.|redis|psycopg|PORT</parameter>
<parameter name="path">/tmp/tmp6vzdzrit</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
</invoke>
<invoke name="Glob">
<parameter name="pattern">**/{test_*.py,*_test.py,conftest.py,docker-compose*.yml,.env*,pytest.ini,tox.ini}</parameter>
<parameter name="path">/tmp/tmp6vzdzrit</parameter>
</invoke>
