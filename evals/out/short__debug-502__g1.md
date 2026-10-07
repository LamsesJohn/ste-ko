502는 프록시나 로드밸런서가 뒤쪽 앱 서버에서 정상 응답을 받지 못한 상태이므로, 프록시 에러 로그부터 확인하세요.

저는 아직 서버에 접속하지 않았습니다. 아래는 일반적인 점검 순서이며 nginx 기준입니다.

1. 프록시 에러 로그를 봅니다: `tail -n 100 /var/log/nginx/error.log`
2. 앱 프로세스 상태를 봅니다: `systemctl status <서비스명>`
3. 프록시를 거치지 않고 앱을 직접 호출합니다: `curl -i http://127.0.0.1:<포트>/`
4. 앱 로그를 봅니다: `journalctl -u <서비스명> -n 100`
5. 메모리 부족으로 종료됐는지 봅니다: `dmesg | grep -i oom`
6. 프록시 설정을 검증합니다: `nginx -t`
7. 설정의 upstream 주소, 포트, 소켓 경로를 앱 설정과 대조합니다.

에러 로그 문구별 원인은 다음과 같습니다.

| 로그 문구 | 의심 원인 |
|---|---|
| `connect() failed (111: Connection refused) while connecting to upstream` | 앱이 꺼졌거나 포트가 다릅니다 |
| `upstream prematurely closed connection while reading response header from upstream` | 앱이 요청 처리 중 죽었습니다 |
| `upstream timed out (110: Connection timed out) while reading response header from upstream` | 앱 응답이 너무 느립니다 |
| `connect() to unix:/...sock failed (13: Permission denied)` | 소켓 파일 권한 문제입니다 |

Apache, ALB, Cloudflare 등 다른 구성이면 로그 위치가 다릅니다. 사용 중인 구성과 에러 로그 원문을 알려 주시면 원인을 좁히겠습니다.
