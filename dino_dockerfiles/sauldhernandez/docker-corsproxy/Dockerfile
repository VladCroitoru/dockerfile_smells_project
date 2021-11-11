FROM node:6-alpine

RUN npm install -g corsproxy && npm cache clean

ENV CORSPROXY_PORT=8080
ENV CORSPROXY_HOST=0.0.0.0
EXPOSE 8080

CMD [ "/usr/local/bin/corsproxy" ]
