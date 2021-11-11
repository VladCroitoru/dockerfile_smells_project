FROM golang:alpine as build
COPY . /go/src/kohlbau.de/x/go-redirect
WORKDIR /go/src/kohlbau.de/x/go-redirect
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -a -installsuffix cgo -o go-redirect main.go

FROM scratch
COPY --from=build /go/src/kohlbau.de/x/go-redirect/go-redirect /bin/
EXPOSE 8080
VOLUME [ "/data" ]
ENTRYPOINT ["/bin/go-redirect"]
