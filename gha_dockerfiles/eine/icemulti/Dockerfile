# docker build -t elide/icemulti:app - < Dockerfile

FROM alpine
RUN apk -U --no-cache add ca-certificates
WORKDIR /icemulti
EXPOSE 8080
ENTRYPOINT ["./icemulti"]
ADD icemulti-app.tgz /icemulti
