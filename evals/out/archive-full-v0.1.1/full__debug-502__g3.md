**프록시의 오류 로그부터 확인해.** 502는 프록시(nginx, ALB 등)가 뒤쪽 앱 서버에서 정상 응답을 받지 못했다는 뜻이야. 원인은 대부분 앱 서버에 있어.

1. 프록시 오류 로그를 읽어. nginx라면 `/var/log/nginx/error.log`야.
2. 로그 문구로 원인을 나눠.
   - `Connection refused`: 앱이 죽었거나 포트가 달라.
   - `upstream timed out`: 앱이 너무 느리게 응답해.
   - `upstream prematurely closed connection`: 앱이 요청을 처리하다 죽었어.
3. 앱 프로세스가 살아 있는지 확인해. `systemctl status <서비스>` 또는 `docker ps`를 써.
4. 앱이 직접 응답하는지 확인해. `curl -i http://127.0.0.1:<포트>/`를 실행해.
5. 오류가 난 시각의 앱 로그를 읽어. 예: `journalctl -u <서비스> --since "10 min ago"`.
6. 앱이 반복해서 죽으면 메모리 부족을 확인해. `dmesg | grep -i oom`을 실행해.
7. 오류가 시작된 시점의 배포나 설정 변경을 확인해.

내가 네 서버를 직접 확인한 것은 아니야. 위 내용은 502의 일반적인 원인 순서야.

어떤 프록시를 쓰고 있어? 알려주면 그에 맞는 명령으로 좁혀 줄게.
