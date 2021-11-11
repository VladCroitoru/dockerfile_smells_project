FROM golang:1.10-alpine AS build

WORKDIR /go/src/app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -tags netgo -ldflags '-w -extldflags "-static"' -o muffins .

FROM scratch
COPY --from=build /go/src/app/muffins /bin/muffins
ENTRYPOINT ["/bin/muffins"]
