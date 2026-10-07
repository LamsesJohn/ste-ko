`ConnectionRefusedError: [Errno 111] Connection refused`는 접속하려는 주소와 포트에서 받는 프로그램이 없다는 뜻입니다. 어느 서버인지 알기 위해 프로젝트 파일을 먼저 확인합니다.


<invoke name="Glob">
<parameter name="pattern">**/*</parameter>
<parameter name="path">/tmp/tmp6vzdzrit</parameter>
</invoke>

<invoke name="Grep">
<parameter name="pattern">localhost|127\.0\.0\.1|connect\(|create_connection|redis|postgres|HOST|PORT</parameter>
<parameter name="path">/tmp/tmp6vzdzrit</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
</invoke>
