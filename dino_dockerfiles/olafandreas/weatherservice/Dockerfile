FROM golang:1.10
WORKDIR /go/src/github.com/olafandreas/weatherservice
RUN go get -u github.com/mattn/go-sqlite3
RUN go get -u github.com/oisann/goxml2json
COPY . .
RUN go build -o WeatherService .
EXPOSE 8080
CMD ./WeatherService