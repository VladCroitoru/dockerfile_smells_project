FROM golang:alpine
COPY . /fatalisa-public-api
WORKDIR /fatalisa-public-api
#ENV GIN_MODE release
#EXPOSE 80
RUN go build fatalisa-public-api
#RUN chmod +x /fatalisa-public-api/fatalisa-public-api
#ENTRYPOINT ["/fatalisa-public-api/fatalisa-public-api"]

FROM alpine:latest

# for timezone setting
RUN apk update && \
    apk add --no-cache tzdata && \
    date

COPY --from=0 /fatalisa-public-api/fatalisa-public-api /app
RUN chmod -R +x /app
ENV GIN_MODE release
ENV TZ 'Asia/Jakarta'

COPY set-build-date.sh /set-build-date.sh
RUN chmod +x /set-build-date.sh && /set-build-date.sh

RUN mkdir -p /schedule /data/logs

EXPOSE 80
ENTRYPOINT ["/app"]