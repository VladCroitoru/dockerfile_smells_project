### Build Golang ###
FROM golang:1.16 AS build-backend
WORKDIR /workdir
ENV GO111MODULE="on"
ARG APP_NAME
ARG APP_VERSION
## download packages
COPY go.mod go.sum ./
RUN go mod download
## build
COPY . ./
RUN GOOS=linux go build -ldflags "-X github.com/ShotaKitazawa/kube-portal/cmd/kubeportal.AppName=${APP_NAME} -X github.com/ShotaKitazawa/kube-portal/cmd/kubeportal.AppVersion=${APP_VERSION}" -o app main.go


### Build Next.js ###
FROM node:15.9.0-alpine3.11 AS build-frontend
WORKDIR /workdir
COPY client/ ./
RUN yarn install
RUN yarn build


### Run ###
FROM gcr.io/distroless/base
## copy binary
COPY --from=build-backend /workdir/app .
COPY --from=build-frontend /workdir/out client/out
## Run
ENTRYPOINT ["./app"]

