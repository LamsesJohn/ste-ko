원인은 테스트가 접속하려는 서버가 실행 중이지 않거나 다른 포트에서 실행 중인 것으로 추정합니다. 아직 코드를 확인하지 못했으니 접속 대상을 찾아보겠습니다.


<invoke name="Grep">
<parameter name="pattern">localhost|127\.0\.0\.1|0\.0\.0\.0|PORT|connect\(</parameter>
<parameter name="path">/tmp/tmp6vzdzrit</parameter>
<parameter name="output_mode">content</parameter>
<parameter name="-n">true</parameter>
</invoke>
<invoke name="Glob">
<parameter name="pattern">**/*{test,conftest,docker-compose,.env}*</parameter>
<parameter name="path">/tmp/tmp6vzdzrit</parameter>
</invoke>
