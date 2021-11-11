FROM node:boron
MAINTAINER mac0314 <rladudals02@gmail.com>

# 앱 디렉토리 생성
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# 앱 의존성 설치
COPY package.json /usr/src/app/
RUN npm install

# 앱 소스 추가
COPY . /usr/src/app

EXPOSE 3000
# config folder 없음
# CMD [ "npm", "start" ]
