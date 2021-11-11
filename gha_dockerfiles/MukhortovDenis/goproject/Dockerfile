FROM golang:1.17.1

WORKDIR /goproject/
ADD ./ /goproject/

RUN go mod download

RUN go build -o goproj ./cmd/web

CMD [ "./goproj" ]