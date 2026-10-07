먼저 작업 디렉터리에서 테스트가 접속하는 호스트와 포트를 찾아보겠습니다.


<invoke name="Grep">
<parameter name="pattern">localhost|127\.0\.0\.1|connect\(|create_connection|PORT|redis|postgres|requests\.(get|post)</parameter>
<parameter name="path">/tmp/tmpci3kw87i</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
<parameter name="head_limit">50</parameter>
</invoke>
<invoke name="Glob">
<parameter name="pattern">**/*{test,docker-compose,compose}*</parameter>
<parameter name="path">/tmp/tmpci3kw87i</parameter>
</invoke>
