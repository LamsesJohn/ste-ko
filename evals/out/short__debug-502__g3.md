앱 프로세스가 살아 있는지부터 확인하세요. 502는 프록시가 업스트림에서 올바른 응답을 받지 못했다는 뜻입니다.

이 서버에서는 아직 아무것도 확인하지 않았습니다. 아래는 일반적인 점검 순서입니다.

1. `systemctl status <서비스명>` 또는 `docker ps`로 앱 프로세스 상태를 봅니다.
2. `curl -i http://127.0.0.1:<포트>/`로 프록시를 거치지 않고 앱에 직접 요청합니다.
3. 프록시 오류 로그를 봅니다. nginx는 `/var/log/nginx/error.log`입니다.
4. `journalctl -u <서비스명> -n 100`으로 앱 로그에서 크래시와 OOM을 찾습니다.
5. `nginx -t`로 설정을 검사하고 업스트림 주소와 포트를 앱 설정과 대조합니다.
6. `free -h`와 `df -h`로 메모리와 디스크 여유를 봅니다.

nginx 오류 로그 문구별 의미는 다음과 같습니다.

| 로그 문구 | 가능한 원인 |
|---|---|
| `connect() failed (111: Connection refused)` | 앱이 죽었거나 포트가 다릅니다 |
| `upstream prematurely closed connection` | 앱이 요청 처리 중 종료되었습니다 |
| `upstream timed out (110: Connection timed out)` | 앱 응답이 타임아웃보다 느립니다 |

프록시 종류(nginx, ALB 등)와 오류 로그 해당 줄을 주시면 원인을 더 좁힐 수 있습니다.
