먼저 업스트림 앱이 실행 중인지 확인합니다. 502는 프록시(Nginx, ALB 등)가 뒤쪽 앱에서 올바른 응답을 받지 못했다는 뜻이기 때문입니다.

1. 앱 프로세스 상태를 확인합니다. 예: `systemctl status <서비스>` 또는 `docker ps`
2. 앱이 기대한 포트에서 응답하는지 확인합니다. 예: `curl -i http://127.0.0.1:<포트>/`
3. 프록시 오류 로그를 읽습니다. Nginx는 보통 `/var/log/nginx/error.log`입니다. `connect() failed`, `upstream prematurely closed`, `timed out` 중 어느 문구인지 봅니다.
4. 앱 로그에서 같은 시각의 크래시, 메모리 부족(OOM), 재시작 기록을 찾습니다.
5. 프록시 설정의 upstream 주소와 포트가 앱의 실제 주소와 같은지 확인합니다.

로그 문구로 원인을 좁힐 수 있습니다.

| 로그 문구 | 가능한 원인 |
|---|---|
| `connection refused` | 앱이 꺼져 있거나 포트가 다릅니다 |
| `prematurely closed` | 앱이 요청 처리 중에 죽었습니다 |
| `timed out` | 앱이 너무 느리거나 멈췄습니다 |

어떤 프록시나 배포 환경(Nginx, ALB, Kubernetes 등)을 쓰는지 알려 주시면 해당 환경의 명령으로 좁혀 드리겠습니다.
