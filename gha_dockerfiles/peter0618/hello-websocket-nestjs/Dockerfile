# for down-sized docker image
FROM node:14-alpine

# APP_ENV 의 기본값은 "prod" 로 설정하지 않아야 합니다.
ARG APP_ENV="dev"

#
ENV APP_ENV=$APP_ENV

#
ENV NODE_ENV=production

#
ENV TZ=Asia/Seoul

#
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# /app 을 application root 로 사용합니다.
WORKDIR /app

# npm install 에 필요한 것들만 복사. packge.json, packeg-lock.json
COPY ./package.json ./yarn.lock ./

# 의존성 설치 및 프로젝트 빌드
RUN yarn install --production=false

# build 할 떄 필요한 것들도 복사
COPY ./tsconfig.json ./tsconfig.build.json ./nest-cli.json ./

# source code 복사
COPY ./src ./src

# source code 복사
COPY ./views ./views

# 의존성 설치 및 프로젝트 빌드
RUN yarn build

# port 노출
EXPOSE 3000

# application 실행
CMD node dist/main
