FROM golang:1.17.1-buster

RUN go version
ENV GOPATH=/

COPY ./ ./ ./
RUN cd ./migrations && ls

# install psql
RUN apt-get update
RUN apt-get -y install postgresql-client

# make wait-for-postgres.sh executable
RUN chmod +x wait-for-postgres.sh

# build go app
RUN go mod download
RUN go build -o app ./cmd/weather-app/main.go

CMD ["./app"]