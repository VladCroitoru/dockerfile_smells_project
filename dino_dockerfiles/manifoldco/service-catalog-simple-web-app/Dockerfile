FROM golang
WORKDIR /go/src/github.com/manifoldco/service-catalog-simple-web-app

COPY main.go .
RUN CGO_ENABLED=0 go build -o app .

FROM scratch
WORKDIR /
COPY --from=0 /go/src/github.com/manifoldco/service-catalog-simple-web-app/app .

EXPOSE 80
ENTRYPOINT ["/app"]
