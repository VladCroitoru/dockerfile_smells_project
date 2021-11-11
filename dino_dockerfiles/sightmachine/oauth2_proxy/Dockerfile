FROM golang:1.9 AS build

WORKDIR /go/src/app

COPY . .

RUN wget -O /usr/bin/dep https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64 \
 && chmod +x /usr/bin/dep \
 && dep ensure -v\
 && go build -o oauth2_proxy

FROM debian:stable-slim
EXPOSE 8080 4180

RUN apt-get update && apt-get install -y wget ca-certificates \
 && wget https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64.deb \
 && dpkg -i dumb-init_*.deb \
 && rm -rf /var/lib/apt/lists/*

COPY --from=build /go/src/app/oauth2_proxy /usr/bin/

ENTRYPOINT [ "/usr/bin/dumb-init", "--", "/usr/bin/oauth2_proxy" ]
CMD [ "--upstream=http://0.0.0.0:8080/", "--http-address=0.0.0.0:4180"]
