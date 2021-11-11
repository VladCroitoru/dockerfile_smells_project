FROM golang as builder

RUN go env -w GO111MODULE=auto \
  && go env -w CGO_ENABLED=0 \
  && go env -w GOPROXY=https://goproxy.cn,https://gocenter.io,https://goproxy.io,direct \
  && go get golang.org/x/net/websocket

WORKDIR /usr/src/app

COPY ./main.go ./
RUN go build -ldflags "-s -w -extldflags '-static'" -o maotama-server main.go

FROM node:buster-slim

RUN apt update && \
	env DEBIAN_FRONTEND=noninteractive apt -y install dnsutils cron tzdata && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  cp -rf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
  echo "Asia/Shanghai" > /etc/timezone && \
  npm -g install pm2 && \
  ln -s /dev/stdout /var/log/cron.log && \
  echo '0 3 * * * /usr/local/bin/pm2 restart maotama-server' > /etc/cron.d/restart-maotama && \
  crontab /etc/cron.d/restart-maotama

COPY ./entrypoint.sh /data/
COPY --from=builder /usr/src/app/maotama-server /usr/bin/
COPY ./pm2.json /data/

WORKDIR /data

ENV TZ Asia/Shanghai

ENTRYPOINT [ "/data/entrypoint.sh" ]
CMD [ "pm2-docker", "/data/pm2.json" ]
