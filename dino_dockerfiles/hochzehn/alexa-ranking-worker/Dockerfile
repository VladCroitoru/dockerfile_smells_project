FROM node:6.2.0

RUN npm install -g detectjs

ADD ./app /opt/app

WORKDIR /opt/app

ENTRYPOINT ["./entrypoint.sh"]
