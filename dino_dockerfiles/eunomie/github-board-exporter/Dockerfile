FROM golang:1.9 as build

WORKDIR /go/src/app
COPY . .

RUN go-wrapper download
RUN go-wrapper install

FROM gcr.io/distroless/base
COPY --from=build /go/bin/app /
CMD ["/app"]