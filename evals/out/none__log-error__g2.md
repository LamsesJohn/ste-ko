로그만으로는 어떤 연결인지 알 수 없어서, 먼저 프로젝트에서 테스트가 접속하려는 대상을 확인해 볼게요.


<invoke name="Bash">
<parameter name="command">cd /tmp/tmp1nzl0htd && ls -la && grep -rnE "localhost|127\.0\.0\.1|HOST|PORT|connect\(" --include=*.py --include=*.env --include=*.yml --include=*.yaml --include=*.toml --include=*.ini --include=*.cfg . 2>/dev/null | head -50</parameter>
</invoke>
<br>


<invoke name="Glob">
<parameter name="pattern">**/*test*</parameter>
</invoke>
<br>
