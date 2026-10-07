**앱 서버(업스트림)부터 확인해. 프록시가 아니라 그 뒤의 앱이 원인인 경우가 가장 많아.** 502는 nginx나 로드밸런서 같은 프록시가 앱에서 정상 응답을 받지 못했다는 뜻이야.

1. 앱 프로세스가 떠 있는지 확인해. `systemctl status <서비스명>` 또는 `docker ps`를 실행해.
2. 프록시를 거치지 않고 앱을 직접 호출해. `curl -i http://127.0.0.1:<포트>/`를 실행해.
3. 프록시 오류 로그를 읽어. nginx는 보통 `/var/log/nginx/error.log`에 있어.
4. 앱 로그에서 크래시를 찾아. `journalctl -u <서비스명> -n 100`을 실행해.
5. 메모리 부족으로 종료됐는지 확인해. `dmesg | grep -i oom`을 실행해.
6. 프록시 설정의 upstream 주소와 포트가 앱이 듣는 주소와 같은지 비교해.
7. 최근 배포나 설정 변경이 있었는지 확인해.

프록시 오류 로그의 문구로 원인을 좁힐 수 있어.

| 로그 문구 | 의미 |
|---|---|
| `connect() failed (111: Connection refused)` | 앱이 꺼져 있거나 포트가 다름 |
| `upstream prematurely closed connection` | 앱이 응답 도중 죽음 |
| `upstream timed out` | 앱이 너무 느림 (이 경우 502가 아니라 504가 나올 때가 많음) |
| `no live upstreams` | 모든 백엔드가 비정상 상태 |

프록시 종류와 앱 실행 방식(systemd, Docker 등)을 알려주면 정확한 명령으로 다시 정리해 줄게.
