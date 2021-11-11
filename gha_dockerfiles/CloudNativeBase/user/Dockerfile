FROM cnbattle/docker-go:builder as builder

WORKDIR /app
COPY . .
#RUN go env -w GO111MODULE=on && go env -w GOPROXY=https://goproxy.cn,direct
RUN make build

FROM cnbattle/docker-go:runner

RUN echo 'Asia/Shanghai' >/etc/timezone

WORKDIR /www

COPY --from=builder  /app/whats /www/whats

EXPOSE 8080

ENTRYPOINT ["/www/whats","web"]