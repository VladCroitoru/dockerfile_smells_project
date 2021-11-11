FROM golang:1.5

# Install dependencies packages
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        libltdl-dev \
        mariadb-server \
        rabbitmq-server \
        mariadb-client-core-10.0 \
        nodejs \
        rsyslog \
        softhsm \

 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 4000

RUN go get -v \
    github.com/jsha/listenbuddy \
    bitbucket.org/liamstask/goose/cmd/goose \
    github.com/golang/lint/golint

ENV GO15VENDOREXPERIMENT 1
WORKDIR /go/src/github.com/letsencrypt/boulder

RUN mkdir -p /go/src/github.com/letsencrypt \
 && git clone https://github.com/letsencrypt/boulder.git /go/src/github.com/letsencrypt/boulder \
 && cd /go/src/github.com/letsencrypt/boulder \
 && git reset --hard e45cd826f7cc207a063df6b0130c52395d3e481b \
 && rm -rf .git
 # 5/16/2016

# Warmup
RUN service mysql start \

 && sh -c 'echo "127.0.0.1 boulder boulder-mysql boulder-rabbitmq" >> /etc/hosts' \
 && test/create_db.sh \

 && service mysql stop

RUN GOBIN=/go/src/github.com/letsencrypt/boulder/bin go install  ./...

ENV BOULDER_MYSQL_PORT=43306
ENV BOULDER_AMQP_PORT=45672
ENV BOULDER_PORT=4000
ENV BOULDER_CALLBACK_PORT=5002

COPY config/rate-limit-policies.yml /go/src/github.com/letsencrypt/boulder/test
COPY bin/entrypoint.sh /usr/bin

ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]
CMD [ "./start.py" ]
