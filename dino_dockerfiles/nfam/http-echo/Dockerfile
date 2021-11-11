# build
FROM golang:1.9.4-alpine3.7
RUN mkdir /http-echo
WORKDIR /http-echo
COPY main.go /http-echo/
ENV CGO_ENABLED=0
ENV GOOS=linux
RUN go build  -ldflags '-w -s' -a -installsuffix cgo -o http-echo

# image
FROM scratch
COPY --from=0 /http-echo/http-echo /
EXPOSE 8080
ENTRYPOINT ["/http-echo"]