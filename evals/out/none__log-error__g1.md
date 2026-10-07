`ConnectionRefusedError: [Errno 111]`은 접속하려는 호스트:포트에서 아무 프로세스도 listen하고 있지 않다는 뜻입니다. 이 프로젝트에서 어떤 서비스에 연결하려는지 먼저 확인해 보겠습니다.


<invoke name="Glob">
<parameter name="pattern">**/*</parameter>
</invoke>
<invoke name="Grep">
<parameter name="pattern">localhost|127\.0\.0\.1|connect\(|create_connection|requests\.|redis|psycopg|HOST|PORT</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
</invoke>
