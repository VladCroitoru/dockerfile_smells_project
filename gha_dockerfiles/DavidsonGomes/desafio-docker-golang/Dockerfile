# repositorio docker davidsongomes/codeeducation
FROM golang:latest AS builder

RUN mkdir code

WORKDIR /code

RUN go mod init codeeducation/rocks

COPY main.go .

RUN go build

FROM scratch

COPY --from=builder /code/rocks ./

CMD ["./rocks"] 