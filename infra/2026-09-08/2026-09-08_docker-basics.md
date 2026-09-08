# Docker 기초: 이미지, 컨테이너, 네트워크와 볼륨

## 1. 전체 관계

```text
🖥️ EC2 또는 로컬 컴퓨터
└─ 🐳 Docker
   ├─ 📄 Dockerfile: 이미지를 만드는 방법
   ├─ 📦 Image: 실행환경과 애플리케이션을 담은 패키지
   ├─ 🐳 Container: 이미지를 실제로 실행한 인스턴스
   ├─ 🛣️ Network: 컨테이너 사이의 통신 통로
   ├─ 💾 Volume: 컨테이너와 분리해 유지하는 데이터 저장공간
   └─ 📋 Compose: 여러 컨테이너의 실행 구성을 관리
```

## 2. 이미지와 컨테이너

Dockerfile로 이미지를 만들고, 이미지를 실행하면 컨테이너가 생성된다.

```text
📄 Dockerfile
   │ docker build
   ▼
📦 my-app:1.0
   │ docker run
   ▼
🐳 Spring 컨테이너
```

- 이미지는 실행 전의 원본 패키지다.
- 컨테이너는 이미지가 실제로 실행되는 격리된 공간이다.
- 하나의 이미지로 여러 컨테이너를 실행할 수 있다.
- 컨테이너를 재시작해도 생성에 사용한 기존 이미지가 유지된다.
- 새 코드를 적용하려면 새 이미지를 만들고 컨테이너를 다시 생성해야 한다.

### 이미지 태그

```text
my-app:1.0
my-app:1.1
my-app:a84f12c
my-app:latest
```

태그는 이미지를 구분하는 이름이다. 운영 배포에서는 `latest`에만 의존하기보다 버전이나 Git 커밋 ID처럼 추적 가능한 태그를 사용하는 것이 롤백에 유리하다.

## 3. CI/CD에서 Docker 이미지가 배포되는 흐름

Jenkins는 정해진 배포 단계를 자동으로 실행하는 도구다.

```text
📝 Git Push
   ▼
⚙️ Jenkins
   ├─ 빌드
   ├─ 테스트
   ├─ Docker 이미지 생성
   └─ 이미지 레지스트리에 Push
            ▼
        🏬 Registry
            │ Pull
            ▼
        🖥️ 운영 서버
            │
            └─ 새 컨테이너 실행
```

- CI: 빌드, 테스트, 이미지 생성처럼 배포 가능한 결과물을 준비한다.
- CD: 준비된 이미지를 운영 서버에 배포하고 실행한다.
- Blue-Green 배포에서는 새 환경을 실행하고 헬스체크를 통과한 뒤 트래픽을 전환한다.

## 4. Docker 네트워크

컨테이너는 서로 다른 실행 공간이다. Docker 네트워크는 컨테이너들이 통신할 수 있는 내부 통로를 제공한다.

```text
🛣️ Compose 기본 네트워크
├─ 🌐 nginx
├─ ☕ backend
└─ 🗄️ db
```

같은 Compose 네트워크에서는 컨테이너 IP를 직접 사용하는 대신 서비스 이름으로 접근할 수 있다.

```text
🌐 Nginx → backend:8080
☕ Spring → db:3306
```

`localhost`는 항상 현재 컨테이너 자신을 뜻한다. Spring과 MySQL이 서로 다른 컨테이너라면 Spring에서 `localhost:3306`이 아니라 `db:3306`처럼 MySQL 서비스 이름을 사용해야 한다.

## 5. 포트 매핑

```yaml
ports:
  - "9000:8080"
```

앞은 호스트 포트, 뒤는 컨테이너 포트다.

```text
🧑 사용자 → 🖥️ 호스트:9000 → 🐳 컨테이너:8080 → ☕ Spring
```

같은 Docker 네트워크의 컨테이너끼리 통신할 때는 컨테이너 내부 포트를 사용한다.

## 6. 볼륨

볼륨은 이미지 버전이 아니라 컨테이너와 분리된 데이터 저장공간이다.

```text
🐳 MySQL 컨테이너 ──▶ 💾 db-data 볼륨
       삭제                     유지

🐳 새 MySQL 컨테이너 ──▶ 💾 기존 db-data 연결
```

컨테이너 내부에만 저장한 데이터는 컨테이너 삭제 시 사라질 수 있다. DB 데이터처럼 유지해야 하는 파일은 볼륨이나 외부 저장소에 저장한다.

볼륨은 DB 전용이 아니다. 컨테이너가 교체되어도 유지해야 하는 파일에 사용할 수 있다. 여러 서버가 파일을 공유해야 한다면 로컬 볼륨 대신 S3 같은 외부 저장소가 더 적합할 수 있다.

## 7. MySQL 컨테이너 초기화

```yaml
services:
  db:
    image: mysql:8
    environment:
      MYSQL_DATABASE: app
      MYSQL_USER: appuser
      MYSQL_PASSWORD: example-password
      MYSQL_ROOT_PASSWORD: example-root-password
    volumes:
      - db-data:/var/lib/mysql

volumes:
  db-data:
```

최초 실행 시 데이터가 없는 경우 MySQL 이미지의 초기화 과정에서 다음 항목을 만들 수 있다.

- `app` 데이터베이스
- `appuser` 사용자
- 사용자와 관리자 비밀번호

`MYSQL_DATABASE`는 빈 논리 데이터베이스를 만드는 설정이다. 회원이나 주문 테이블은 SQL, JPA 또는 Flyway 같은 마이그레이션 도구로 별도 생성해야 한다.

기존 데이터가 들어 있는 볼륨을 다시 연결하면 초기화 환경변수를 바꾸더라도 기존 DB가 자동으로 다시 만들어지지는 않는다.

## 8. Compose 예시

```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    depends_on:
      - backend

  backend:
    image: my-app:1.0
    environment:
      SPRING_DATASOURCE_URL: jdbc:mysql://db:3306/app
      SPRING_DATASOURCE_USERNAME: appuser
      SPRING_DATASOURCE_PASSWORD: example-password
    depends_on:
      - db

  db:
    image: mysql:8
    environment:
      MYSQL_DATABASE: app
      MYSQL_USER: appuser
      MYSQL_PASSWORD: example-password
      MYSQL_ROOT_PASSWORD: example-root-password
    volumes:
      - db-data:/var/lib/mysql

volumes:
  db-data:
```

실제 운영 비밀번호는 Git에 저장되는 Compose 파일에 직접 작성하지 않고 Secret 관리 방법을 사용해야 한다.

## 핵심 요약

> Dockerfile로 이미지를 만들고 이미지를 실행하면 컨테이너가 된다. 컨테이너끼리는 Docker 네트워크로 통신하며, 컨테이너가 교체돼도 유지할 데이터는 볼륨이나 외부 저장소에 둔다. Jenkins는 새 이미지의 빌드·테스트·배포 과정을 자동화할 수 있다.
