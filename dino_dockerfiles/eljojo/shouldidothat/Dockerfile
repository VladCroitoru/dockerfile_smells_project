FROM eljojo/golang-docker

WORKDIR /app
RUN git clone https://github.com/eljojo/shouldidothat.git .

RUN go get -d
RUN go build -o shouldidothat

CMD ["/app/shouldidothat", "-c", "/etc/shouldidothat/conf.json"]

