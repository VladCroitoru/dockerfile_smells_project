FROM golang:1.17-alpine AS build

WORKDIR /build

COPY go.mod ./
COPY go.sum ./

RUN go mod download

COPY . ./

RUN go build -o emotesbot


FROM alpine

COPY --from=build /build/emotesbot /usr/local

ENV PATH="/usr/local:${PATH}"

CMD ["emotesbot"]
