FROM node:alpine

WORKDIR /oauth

COPY . /oauth

ENV CLIENT_ID=abcn82LQg9kXrVsI7CC0QG2Zap6SM6K4REsHQOl0 \
    CLIENT_SECRET=ZDMmLZ7dsMacHhnK8AQLjiKwCb4joFkx2FylADePGKk56nbOJ1zuEyObhiyKLHiGz9dkq3oGLFKrn70dqvc9Zb28ECwovP0WA6TG0SofjO5SwXncsmNoSAOybpgd3Zy4 \
    AUTHORIZE_URI=https://arkid.demo.longguikeji.com/oauth/authorize/ \
    ACCESS_TOKEN_URI=https://arkid.demo.longguikeji.com/oauth/token/ \
    USERINFO_URI=https://arkid.demo.longguikeji.com/oauth/userinfo/ \
    REDIRECT_URI=http://124.70.55.171:8998/oauth/redirect

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g" /etc/apk/repositories &&\
    apk update &&\
    apk add --no-cache tini &&\
    npm install

CMD tini -- node index.js