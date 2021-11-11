FROM golang:latest

RUN go get -t github.com/joho/godotenv \
    && go get -t github.com/labstack/echo \
    && go get -t github.com/DATA-DOG/godog/cmd/godog \
    && go get -t golang.org/x/crypto/bcrypt \
    && go get -t github.com/jinzhu/gorm \
    && go get -t github.com/go-sql-driver/mysql

RUN go get -t os log fmt time bytes errors reflect strconv strings testing net/http encoding/json
