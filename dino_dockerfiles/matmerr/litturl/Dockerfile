FROM golang:alpine as go-stage
ENV LU_DIR=$GOPATH/src/github.com/matmerr/litturl/
WORKDIR $LU_DIR
COPY server server
COPY main.go .
RUN apk add --update git && go get ./...
RUN go build  -o /app/litturl main.go

FROM node:alpine as node-stage
RUN apk add --update git 
WORKDIR /app
COPY client .
RUN npm install && npm rebuild node-sass && npm run build

FROM alpine:latest
WORKDIR /app
COPY conf conf
COPY --from=go-stage /app/litturl .
COPY --from=node-stage /app/dist/ dist/
EXPOSE 8001
CMD ["./litturl", "dist/"]

