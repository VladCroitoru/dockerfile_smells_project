FROM golang:1.9 as gobuilder
WORKDIR /go/src/github.com/ibigbug/ss-account
COPY . .
RUN CGO_ENABLED=0 go build -a -o app -ldflags="-s -w" main.go

FROM node:8 as nodebuilder
WORKDIR /frontend
COPY ./frontend/ /frontend
RUN npm i -g yarn
RUN yarn
RUN ./node_modules/.bin/ng build --prod --base-href /dashboard/

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
ENV GODEBUG=gctrace=1
COPY --from=gobuilder /go/src/github.com/ibigbug/ss-account/app .
COPY --from=nodebuilder /frontend/dist/ ./public
CMD [ "./app" ]
