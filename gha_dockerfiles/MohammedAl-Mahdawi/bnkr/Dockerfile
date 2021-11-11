#build stage
FROM golang:alpine AS builder
RUN apk add build-base
WORKDIR /go/src/app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a *.go

FROM mariadb:10.5.9-focal
ARG TARGETPLATFORM

RUN apt update

RUN apt install curl wget -y

# Install kubectl binary
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/${TARGETPLATFORM}/kubectl"
RUN install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Install MongoDB tools
RUN if [ $TARGETPLATFORM = "linux/amd64" ]; then curl https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2004-x86_64-100.3.1.deb --output mongodb-tools.deb; else curl https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2004-arm64-100.3.1.deb --output mongodb-tools.deb; fi

RUN apt install ./mongodb-tools.deb -y
RUN rm ./mongodb-tools.deb

# Install PostgresQL 13
RUN echo "deb http://apt.postgresql.org/pub/repos/apt focal-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt update
RUN apt -y install postgresql-13

RUN apt clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /go/src/app/main /main

ENTRYPOINT /main
