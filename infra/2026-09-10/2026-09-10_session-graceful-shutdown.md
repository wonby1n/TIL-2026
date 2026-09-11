# 다중 서버의 세션과 안전한 종료

## 서버 메모리에 저장한 세션의 문제

로그인 상태를 Spring A 메모리에만 저장하면 다음 요청이 Spring B로 전달됐을 때 로그인 정보를 찾지 못할 수 있다.

```text
🧑 로그인 → ☕ Spring A
              └─ 세션을 A 메모리에 저장

🧑 다음 요청 → ⚖️ LB → ☕ Spring B
                         └─ 세션 없음
```

Spring A가 재시작되면 메모리의 세션도 사라진다.

## 공용 세션 저장소

여러 Spring 서버가 Redis 같은 공용 저장소를 사용하면 어느 서버가 요청을 받아도 로그인 상태를 확인할 수 있다.

```text
             ┌─▶ ☕ Spring A ─┐
🧑 → ⚖️ ALB ─┤               ├─▶ 🧠 Redis
             └─▶ ☕ Spring B ─┘
```

## Sticky Session

로드 밸런서가 같은 사용자의 요청을 가능한 한 동일한 서버에 전달하는 방식이다.

```text
사용자 A → Spring A
사용자 A → Spring A
사용자 B → Spring B
```

구성이 단순해질 수 있지만 특정 서버 장애 시 그 서버 메모리의 세션을 잃을 수 있고 부하가 고르게 분산되지 않을 수 있다.

## Graceful Shutdown

서버를 즉시 강제 종료하면 처리 중인 요청이 끊길 수 있다. Graceful Shutdown은 새 요청 수신을 중단하고 처리 중인 요청을 가능한 범위에서 완료한 뒤 종료한다.

```text
☕ 기존 Spring
├─ 신규 요청 수신 중단
├─ 처리 중인 요청 완료
└─ 안전하게 종료
```

## Connection Draining

로드 밸런서가 서버를 대상에서 제외할 때 기존 연결을 즉시 끊지 않고 진행 중인 요청이 끝날 시간을 주는 방식이다.

```text
⚖️ Load Balancer
├─ 새 요청 → 🟢 Green
└─ 기존 요청 완료 → 🔵 Blue → 종료
```

Blue-Green 전환 직후 Blue를 강제 종료하기보다 Graceful Shutdown과 Connection Draining을 함께 고려하면 진행 중인 요청을 보호하는 데 도움이 된다.

## 핵심 요약

> Spring을 여러 대 운영하려면 특정 서버 메모리에만 상태를 의존하지 않도록 설계하고, 배포 시에는 진행 중인 요청을 마칠 시간을 준 뒤 서버를 종료해야 한다.
