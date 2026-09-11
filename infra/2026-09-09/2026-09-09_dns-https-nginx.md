# DNS, HTTPS와 Nginx 요청 경로

## 전체 요청 흐름

```text
🧑 사용자
 → 📖 DNS
 → 🌍 서버 IP
 → 🔒 HTTPS
 → 🌐 Nginx
 → ☕ Spring
```

## DNS

DNS는 `api.example.com` 같은 도메인을 서버 IP 주소로 연결한다. 서버를 교체했지만 DNS가 이전 IP를 가리키면 요청은 이전 서버로 이동한다.

## HTTP와 HTTPS 포트

- 80번: 일반적인 HTTP 포트
- 443번: 일반적인 HTTPS 포트

Nginx는 80번 HTTP 요청에 443번 HTTPS 주소로 다시 요청하라는 Redirect 응답을 보낼 수 있다. HTTPS 연결에서는 인증서를 이용해 TLS 암호화 통신을 처리한다.

```text
🧑 HTTP :80 → 🌐 Nginx → HTTPS 주소로 Redirect
🧑 HTTPS:443 ══🔒══▶ 🌐 Nginx → ☕ Spring
```

인증서의 도메인과 접속 도메인이 다르거나 유효기간이 끝나면 브라우저가 보안 경고를 표시할 수 있다.

## 리버스 프록시

프록시는 누군가를 대신하는 중간 대리인이다.

```text
포워드 프록시: 🧑 사용자를 대신 → 🕵️ Proxy → 외부 서버
리버스 프록시: 사용자 → 🌐 Proxy → 내부 서버들을 대신
```

Nginx는 경로나 도메인에 따라 요청을 내부 서버로 전달할 수 있다.

```text
🧑 사용자 → 🌐 Nginx
                 ├─ /api → ☕ Backend
                 └─ /ai  → 🤖 AI Server
```

## 프록시 헤더

Spring에서는 요청 상대가 Nginx로 보일 수 있다. Nginx는 원래 사용자와 프로토콜 정보를 다음과 같은 헤더에 전달할 수 있다.

```text
X-Forwarded-For: 실제 사용자 IP
X-Forwarded-Proto: https
```

이 헤더는 신뢰할 수 있는 프록시가 설정한 경우에만 신뢰하도록 구성해야 한다.

## 502와 504

- `502 Bad Gateway`: Nginx가 뒤의 Spring에서 정상적인 응답을 받지 못함
- `504 Gateway Timeout`: Spring 연결 후 제한 시간 안에 응답받지 못함

```text
502: 🌐 Nginx → ☕ Spring 연결 거부·비정상 응답
504: 🌐 Nginx → ☕ Spring → 🗄️ 느린 DB → 시간 초과
```

## 핵심 요약

> DNS가 도메인을 서버로 안내하고 HTTPS가 통신을 보호한다. 리버스 프록시인 Nginx는 내부 서버를 대신해 요청을 전달하며, 502와 504는 뒤쪽 서버 연결과 응답시간 문제를 구분하는 단서가 된다.
