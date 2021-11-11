FROM golang:1.17 as base

FROM base as dev

RUN curl -sSfL https://raw.githubusercontent.com/cosmtrek/air/master/install.sh | sh -s -- -b $(go env GOPATH)/bin

WORKDIR /opt/app/api
CMD ["air"]

FROM base AS backend-builder

WORKDIR /server

COPY ./server .

RUN go mod download

RUN CGO_ENABLED=0 go build -o react-router ./server/main.go


FROM node:16 AS frontend-builder

WORKDIR /frontend

COPY ./web-client/package.json ./web-client/yarn.lock  ./

RUN yarn

RUN yarn global add @angular/cli



