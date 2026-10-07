502(Bad Gateway)는 프록시/게이트웨이(Nginx, ALB 등)가 업스트림 앱 서버에서 유효하지 않은 응답을 받았다는 뜻입니다. 아래 순서로 확인하세요.

**1. 업스트림 앱이 살아 있는지**
- 프로세스/서비스 상태: `systemctl status <앱서비스>`, `ps aux | grep <앱>`, 컨테이너라면 `docker ps`, `docker logs <컨테이너>`
- 앱이 직접 응답하는지: `curl -i http://127.0.0.1:<앱포트>/health`

앱이 죽었거나 포트를 열지 않았다면 대부분 여기서 원인이 나옵니다.

**2. 프록시 에러 로그**
- Nginx: `tail -f /var/log/nginx/error.log`
  - `connect() failed (111: Connection refused)` → 앱이 안 떠 있거나 포트/주소 불일치
  - `upstream prematurely closed connection` → 앱이 요청 처리 중 크래시/종료
  - `upstream sent too big header` → 헤더/쿠키 크기, `proxy_buffer_size` 조정
  - `no live upstreams` → 모든 백엔드가 헬스체크 실패

**3. 앱 로그**
- 예외, OOM, 시작 실패 확인: `journalctl -u <앱서비스> -n 200`
- OOM kill 여부: `dmesg -T | grep -i -E "killed process|out of memory"`

**4. 프록시 설정과 실제 앱의 불일치**
- `proxy_pass`/upstream의 호스트·포트·소켓 경로가 맞는지 (`nginx -T`로 최종 설정 확인)
- Unix 소켓이면 파일 존재와 권한 확인 (gunicorn/php-fpm 등)
- 최근 배포나 설정 변경이 있었는지

**5. 리소스 및 한계**
- CPU/메모리/디스크: `top`, `free -m`, `df -h`
- 워커 수나 연결 한도 초과 (gunicorn workers, php-fpm `pm.max_children`, 파일 디스크립터)

**6. 클라우드 환경이라면**
- ALB/ELB: 타깃 그룹 헬스체크 상태, 보안 그룹, 타깃 포트
- Cloudflare 등 CDN: 오리진 직접 호출 시 정상인지 비교

**빠른 판단 요령**
- 항상 502 → 앱 다운 또는 설정/포트 오류
- 간헐적 502 → 크래시 재시작, 워커 부족, 타임아웃, 배포 중 롤링
- 특정 요청에서만 → 해당 요청 처리 중 앱 크래시나 큰 헤더/응답

사용 중인 스택(Nginx/Apache/ALB, 앱 언어/프레임워크)과 에러 로그 한 줄을 알려주시면 더 구체적으로 짚어드릴게요. 원하시면 이 환경에서 직접 로그나 설정을 확인해 볼 수도 있습니다.
