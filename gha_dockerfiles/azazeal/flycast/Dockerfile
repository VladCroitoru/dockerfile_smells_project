FROM golang:1.17-alpine as build

WORKDIR /build
COPY go.mod go.sum ./
RUN go mod download

COPY . ./
RUN CGO_ENABLED=0 go build -o binary .

FROM alpine
COPY --from=build /build/binary /usr/local/bin/flycast

ENTRYPOINT [ "flycast" ]
