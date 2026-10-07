먼저 리버스 프록시의 error 로그를 확인하세요. 502는 프록시가 업스트림 서버에서 올바른 응답을 받지 못했다는 뜻입니다.

아직 서버나 설정을 직접 확인하지 않았습니다. 아래는 일반적인 점검 순서입니다.

1. 프록시 error 로그를 봅니다. Nginx 기본 경로는 `/var/log/nginx/error.log`입니다.
   ```
   sudo tail -n 100 /var/log/nginx/error.log
   ```
2. 로그 문구로 원인을 좁힙니다.

   | 로그 문구 | 의미 |
   |---|---|
   | `connect() failed (111: Connection refused)` | 업스트림 프로세스가 죽었거나 포트가 다릅니다 |
   | `upstream timed out` | 업스트림 응답이 너무 느립니다 |
   | `upstream prematurely closed connection` | 업스트림 프로세스가 요청 중 비정상 종료했습니다 |
   | `no live upstreams` | 모든 업스트림이 실패 상태입니다 |
   | `connect() to unix:... failed (2: No such file or directory)` | 소켓 경로가 잘못됐거나 소켓이 없습니다 |

3. 업스트림 프로세스 상태를 확인합니다.
   ```
   systemctl status <서비스명>
   ```
4. 업스트림 포트가 열려 있는지 확인합니다.
   ```
   ss -tlnp | grep <포트>
   ```
5. 프록시를 거치지 않고 업스트림에 직접 요청합니다.
   ```
   curl -i http://127.0.0.1:<포트>/
   ```
6. 애플리케이션 로그에서 크래시나 예외를 찾습니다.
   ```
   journalctl -u <서비스명> -n 200 --no-pager
   ```
7. 메모리 부족으로 종료됐는지 확인합니다.
   ```
   dmesg | grep -i -E "oom|killed process"
   ```
8. 최근 배포나 설정 변경이 있었는지 확인합니다. 변경 직후라면 설정 문법을 검사합니다.
   ```
   sudo nginx -t
   ```

CDN이나 로드밸런서(Cloudflare, ALB 등)가 앞단에 있으면 그 계층의 로그도 확인하세요. 502를 낸 계층이 프록시가 아닐 수 있습니다.

사용 중인 프록시 종류와 error 로그 내용을 알려주시면 원인을 더 좁혀 드리겠습니다.
