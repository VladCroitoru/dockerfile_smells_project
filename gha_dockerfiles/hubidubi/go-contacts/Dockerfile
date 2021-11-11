FROM golang:alpine AS builder
RUN apk add curl
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go get -d -v
RUN go build

#EXPOSE 8080
#ENTRYPOINT ["/app/main","--dsn=gocontacts:gocontacts@tcp(host.docker.internal:3306)/gocontacts?charset=utf8&parseTime=true"]

# step 2
FROM alpine
COPY --from=builder /app/main /
EXPOSE 8080
# Command to run
ENTRYPOINT ["/main","--dsn=gocontacts:gocontacts@tcp(host.docker.internal:3306)/gocontacts?charset=utf8&parseTime=true"]