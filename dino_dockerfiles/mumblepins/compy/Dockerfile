FROM alpine:3.7 as compy-builder


RUN apk add --no-cache go curl git libjpeg jpeg-dev libressl build-base
RUN go get -v github.com/mumblepins/compy
RUN rm -r /root/go/src/github.com/mumblepins/compy/ && \
    mkdir -p /root/go/src/github.com/mumblepins/compy/
COPY . /root/go/src/github.com/mumblepins/compy/
WORKDIR /root/go/src/github.com/mumblepins/compy
RUN go get -d -v ./...
RUN go build -v

FROM alpine:3.7

RUN apk add --no-cache libjpeg libstdc++ ca-certificates libwebp-tools

COPY --from=compy-builder /root/go/src/github.com/mumblepins/compy/compy /usr/local/bin/compy
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 9999
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]



