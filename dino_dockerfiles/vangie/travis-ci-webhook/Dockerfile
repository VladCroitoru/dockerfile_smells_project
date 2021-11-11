FROM node:7-alpine

EXPOSE 7777

# Install docker
RUN set -ex && \
    if [ $(wget -qO- ipinfo.io/country) == CN ]; then printf "http://mirrors.ustc.edu.cn/alpine/v3.4/main\nhttp://mirrors.ustc.edu.cn/alpine/v3.4/community" > /etc/apk/repositories ;fi && \
    apk add --update --no-cache docker py-pip bash && \
    pip install docker-compose

ADD . /usr/src/app/
WORKDIR /usr/src/app/
RUN yarn

CMD ["yarn", "start"]
