# Uptime Kuma와 서버 모니터링

## Uptime Kuma의 역할

Uptime Kuma는 서비스 외부에서 웹사이트, API, 포트 등이 정상적으로 응답하는지 주기적으로 검사하고 장애와 복구를 알리는 자체 호스팅 모니터링 도구다.

```text
👀 Uptime Kuma
   ├─▶ 🌐 Nginx 접속 확인
   ├─▶ ☕ Spring /health 확인
   └─▶ 🤖 AI 서버 응답 확인
             ↓ 실패
          🔔 알림
```

서비스 내부 구현을 모르더라도 외부에서 정상 응답하는지 확인하므로 블랙박스 모니터링에 가깝다. 작은 프로젝트에서는 설치와 운영이 간단해 단독으로 사용할 수 있지만, 규모가 커지면 메트릭·로그·트레이스 도구와 함께 사용한다.

## 같은 서버에 설치할 때의 한계

감시 대상과 Uptime Kuma가 같은 EC2에 있으면 EC2 전체가 중단될 때 감시 프로그램도 함께 중단되어 알림을 보내지 못할 수 있다.

```text
EC2 한 대
├─ ☕ 감시 대상 Spring
└─ 👀 Uptime Kuma

EC2 장애 → 둘 다 중단
```

외부 장애까지 탐지해야 한다면 감시 대상과 다른 서버나 외부 환경에 모니터를 두는 편이 안전하다.

## 헬스체크 깊이

Spring 프로세스만 살아 있는지 검사하면 DB 연결이 끊어진 상태를 놓칠 수 있다. 서비스가 실제 요청을 처리하는 데 필요한 의존성까지 확인하도록 헬스체크를 구성할 수 있다.

```text
👀 Kuma → ☕ Spring /health → 🗄️ DB 연결 확인
```

단, 공개 헬스 응답에 DB 주소나 인증정보 같은 내부 정보를 노출하면 안 된다. 단순 생존 여부를 보는 liveness와 실제 요청 처리 준비 상태를 보는 readiness도 목적에 따라 구분한다.

## 장애 이후 로그 확인

Kuma는 장애 시점과 응답 실패를 알려주지만 정확한 원인은 각 프로그램의 로그와 메트릭을 확인해야 한다.

```text
🧑 요청 → 🌐 Nginx 로그 → ☕ Spring 로그 → 🗄️ DB 로그
```

Docker 컨테이너 로그 확인 예시:

```bash
docker ps
docker logs --tail 100 -f spring-container

docker compose logs -f nginx
docker compose logs -f backend
docker compose logs -f db
```

Nginx의 일반적인 로그 위치는 다음과 같지만 실제 경로는 설정에 따라 다를 수 있다.

```text
/var/log/nginx/access.log  # 요청 기록
/var/log/nginx/error.log   # 프록시 연결 실패 등 오류
```

- `502`: Nginx가 뒤쪽 Spring 서버에서 정상 응답을 받지 못한 경우 등을 확인한다.
- `Connection refused`: 대상 프로세스 종료 또는 주소·포트 오류 등을 확인한다.
- `Connection timed out`: 네트워크, 방화벽 또는 대상 서버의 지연 등을 확인한다.
- `Too many connections`: DB 연결 한도와 커넥션 사용 상태 등을 확인한다.

오류 문구 하나만으로 원인을 확정하지 않고 앞뒤 로그, 설정과 메트릭을 함께 확인해야 한다.

## 규모가 커질 때의 관측 도구

| 목적 | 도구 예시 |
|---|---|
| 외부 가동 여부 | Uptime Kuma, 클라우드 헬스체크 |
| CPU·메모리·요청량 | Prometheus, CloudWatch |
| 대시보드 | Grafana |
| 중앙 로그 검색 | ELK, Loki, CloudWatch Logs |
| 요청 경로 추적 | OpenTelemetry, Jaeger, APM |
| 알림 관리 | Alertmanager, Slack 연동 |

## 핵심 요약

> Uptime Kuma로 서비스가 외부에서 살아 있는지 확인하고, 장애가 감지되면 Nginx에서 Spring과 DB 방향으로 로그·메트릭·트레이스를 따라가며 원인을 좁힌다.
