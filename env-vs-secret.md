# .env vs secrets manager

## .env
### 지금 어떻게 쓰고 있나
- 서비스마다 .env 파일을 사용해서 보안 암호를 관리하고있다
- .env 파일은 수작업으로 만들어지고 아마존 S3 버킷에 저장된다
- `pre` 랑 `live` 각각 환경 값이 있다
- .env 파일은 CI/CD 빌드 할때 배포 전 단계에서 적용된다
  - 예: https://gitlab.com/gbike-dev-team/gbike-labs-admin/-/blob/develop/.gitlab-ci.yml#L28

### 쓰는 이유
- 암호를 코드에 저장하면 안되니깐 .env 파일을 쓴다

### 단점
- 빌드 타임때 적용이 되서 만약 암호를 바꿔야 되면 배포를 다시 해야된다
- 각각 서비스랑 환경 마다 파일이 있어서 관리해야될 갯수가 많고 변경하는게 번거로울수 있다
  - 공용 암호가 여러 서비스에 사용 된다면 바꿔야할 파일들을 일일히 찾아서 업데이트 해야된다
  - 바꿔야하는 면적이 클수록 실수 할수 있는 확률이 높다
- 암호를 바꾸려면 서비스가 다운 될수 있다
- 쉽게 암호 rotation 을 못한다
- .env 파일을 개발자들끼리 공유할때 (slack 또는 이메일로) unencrypted 상태로 주고받으면 비밀이 유출 될수 있다


## Secrets Manager
- 비밀이랑 배포 싸이클이랑 decouple 할수 있어서 좋다
- 비밀을 AWS 에 저장 해놓으면 runtime 때 불러다 쓴다
- 비밀을 쉽게 바꿀수 있다
- 비밀 rotation 을 할수 있어 비밀 유출이 되도 리스크를 줄일수 있다
- 비밀은 한곳에 저장 해놓고 여러 서비스에서 불러 써도 된다
  - 비밀을 복제 안해도 된다

### 주의햐야할 점 (리스크)
- 비밀 한번 잘못 바꾸면 여러 서비스 장애 생길수 있음
  - 비밀 바꿀수 있는 권한 또는 절차를 까다롭게 만들어야함
  - 아무나 못 바꾸게 해야됨

## 참고 자료
- Managing secrets
  - https://www.doppler.com/blog/why-syncing-env-files-doesnt-scale-for-secrets-management
  - https://www.opensourceforu.com/2022/02/managing-secrets-with-secretsfoundry/
  - https://developers.refinitiv.com/en/article-catalog/article/how-to-separate-your-credentials--secrets--and-configurations-fr
- Spring Boot AWS Secrets Manager 연동
  - https://leesungki.github.io/gatsby-springboot-study-secretsManager/
- AWS Secrets Manager
  - 영어 - https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
  - 한국어 - https://docs.aws.amazon.com/ko_kr/secretsmanager/latest/userguide/intro.html
- Why rotate secrets?
  - https://www.akeyless.io/secrets-management-glossary/secret-rotation/
  - 