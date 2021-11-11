FROM alpine:3.3

WORKDIR /usr/src

RUN apk add --no-cache build-base libusb libusb-dev git && git clone https://github.com/todbot/blink1.git && cd blink1/commandline/ && make OS=linux all blink1-tiny-server && make install && cp blink1-tiny-server /usr/local/bin/ && apk del build-base libusb-dev git && rm -fr /usr/src/blink1

EXPOSE 8080

CMD ["blink1-tiny-server", "-p", "8080"]
