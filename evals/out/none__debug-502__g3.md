502(Bad Gateway)는 프록시/게이트웨이(nginx, ALB 등)가 업스트림 앱 서버에서 올바른 응답을 받지 못했다는 뜻입니다. 아래 순서로 확인하세요.

**1. 업스트림 앱이 살아 있는지**
- 프로세스/서비스 상태: `systemctl status <앱서비스>`, `docker ps`, `pm2 ls`
- 앱이 직접 응답하는지: `curl -i http://127.0.0.1:<앱포트>/` (프록시를 우회해서 확인)
- 포트 리스닝 여부: `ss -ltnp | grep <포트>`

**2. 프록시 에러 로그** (가장 빠른 단서)
- nginx: `tail -n 100 /var/log/nginx/error.log`
  - `connect() failed (111: Connection refused)` → 앱이 죽었거나 포트가 다름
  - `upstream prematurely closed connection` → 앱이 요청 처리 중 크래시
  - `upstream timed out` → 앱이 느림 (이 경우 504가 더 흔함)
  - `no live upstreams` → 헬스체크 전부 실패

**3. 앱 로그**
- `journalctl -u <앱서비스> -n 200 --no-pager` 또는 `docker logs --tail 200 <컨테이너>`
- OOM kill, 예외 스택트레이스, 시작 실패 여부 확인
- OOM 의심 시: `dmesg -T | grep -i -E 'killed process|out of memory'`

**4. 최근 변경 사항**
- 배포, 설정 변경, 환경변수/시크릿 변경, 의존성 업데이트가 있었는지

**5. 프록시 설정**
- `proxy_pass`의 주소/포트/소켓 경로가 맞는지, `nginx -t`로 문법 확인
- unix 소켓이면 파일 존재 및 권한 확인
- Docker/k8s라면 서비스명/DNS, 컨테이너 간 네트워크 확인

**6. 리소스**
- `df -h`(디스크), `free -m`(메모리), `top`(CPU), 파일 디스크립터 한도

**7. 간헐적인 502라면**
- 워커 수/커넥션 한도 부족, keepalive 타임아웃 불일치(프록시 > 앱일 때 발생), 배포 중 롤링 재시작 타이밍 확인

보통은 **2번(프록시 에러 로그) → 1번(앱 직접 호출)** 순서로 보면 원인이 대부분 좁혀집니다. 사용 중인 스택(nginx/ALB/Kubernetes 등)과 에러 로그 내용을 알려주시면 더 구체적으로 도와드릴게요. 원하시면 이 환경에서 직접 로그나 설정을 확인해 볼 수도 있습니다.
