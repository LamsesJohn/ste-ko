502 Bad Gateway는 "프록시/게이트웨이는 살아 있는데, 그 뒤의 업스트림(앱 서버)에서 잘못된 응답을 받았거나 연결에 실패했다"는 뜻입니다. 아래 순서로 확인하면 빠릅니다.

**1. 업스트림 앱이 살아 있는지**
```bash
systemctl status <앱서비스>        # 또는 docker ps / pm2 status / kubectl get pods
ss -ltnp | grep <앱포트>           # 앱이 해당 포트에서 listen 중인지
curl -i http://127.0.0.1:<앱포트>/health   # 프록시를 거치지 않고 직접 호출
```
직접 호출이 실패하면 문제는 앱 쪽입니다(크래시, OOM, 기동 실패, 포트 불일치).

**2. 프록시 에러 로그**
```bash
tail -n 100 /var/log/nginx/error.log
```
메시지별 의미:
- `connect() failed (111: Connection refused)` → 앱이 죽었거나 포트/주소가 틀림
- `upstream prematurely closed connection` → 앱이 요청 처리 중 크래시
- `upstream timed out` → 앱이 느림 (이 경우 보통 504지만 설정에 따라 502도 가능)
- `no live upstreams` → 모든 업스트림이 비정상으로 표시됨
- `connect() to unix:/...sock failed (13/2)` → 소켓 권한 또는 경로 문제

**3. 앱 로그와 시스템 로그**
```bash
journalctl -u <앱서비스> -n 200 --no-pager
dmesg -T | grep -i -E "killed process|oom"   # OOM kill 여부
```

**4. 최근 변경 사항**
배포, 설정 변경, 인증서/환경변수 변경, 디스크 가득 참(`df -h`), 메모리 부족(`free -m`)을 확인하세요.

**5. 프록시 설정**
```bash
nginx -t
grep -rn "proxy_pass\|upstream\|fastcgi_pass" /etc/nginx/
```
`proxy_pass`의 주소/포트가 실제 앱과 일치하는지, DNS가 바뀌었는데 nginx가 옛 IP를 캐시하고 있지는 않은지 봅니다(재시작/reload로 확인).

**자주 나오는 원인 요약**
- 앱 프로세스 다운/재시작 루프 (가장 흔함)
- 메모리 부족으로 OOM kill
- 포트나 소켓 경로 불일치
- PHP-FPM/gunicorn 워커 고갈
- 앞단에 CDN/로드밸런서(Cloudflare, ALB 등)가 있을 때 오리진 문제

어떤 스택(nginx/Apache, Docker, k8s, 클라우드 LB 등)인지, 에러 로그의 해당 줄을 알려주시면 원인을 더 좁혀드릴 수 있습니다. 원하시면 이 작업 디렉터리에서 설정 파일이나 로그를 직접 살펴볼 수도 있습니다.
