FROM golang:1.16

ARG app_name

RUN mkdir -p /go/src/github.com/Blackmocca/opentracing-example
WORKDIR /go/src/github.com/Blackmocca/opentracing-example

ENV GO111MODULE=on
ENV ADDR=0.0.0.0
ENV TZ=Asia/Bangkok

# Copy app service 
COPY go.mod .
COPY . .

RUN go mod tidy     

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o   /go/src/github.com/Blackmocca/opentracing-example/build/app main.go

FROM amd64/alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /usr/app

COPY --from=0 /go/src/github.com/Blackmocca/opentracing-example/build/app .
COPY --from=0 /go/src/github.com/Blackmocca/opentracing-example/assets assets
COPY --from=0 /go/src/github.com/Blackmocca/opentracing-example/migrations migrations

EXPOSE 3000
EXPOSE 3100

CMD ["./app"]  

