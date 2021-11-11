FROM node:12.18.3 as builder

# 이미지 빌드에만 사용되기 때문에 라벨을 builder로 설정. Jenkins 파이프라인에서 이미지 빌드 이후 자동으로 삭제시키기 위함.
LABEL stage=builder

# node.js 임시 컨테이너에 작업 폴더를 생성하고 그 안에 package.json을 복사해서 넣음.
# 이 컨테이너에서 yarn을 사용해서 의존성 패키지를 설치하고, 빌드를 함.
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY package.json /usr/src/app/package.json

# 컨테이너 밖에 있는 소스를 컨테이너 안 작업폴더로 복사하고 빌드
COPY . /usr/src/app
RUN yarn
RUN yarn build

# 실제 컨테이너에 사용할 이미지를 만들기 시작함.
FROM nginx:latest

# nginx의 기본 설정을 앱에서 설정한 파일로 덮어쓰기
COPY conf/default.conf /etc/nginx/conf.d/default.conf

# 위에서 생성한 앱의 빌드산출물을 nginx의 샘플 앱이 사용하던 폴더로 이동
COPY --from=builder /usr/src/app/build /usr/share/nginx/html

# 타임존 추가
ENV TZ=Asia/Seoul

# 3000 포트 오픈하고 nginx 실행
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]