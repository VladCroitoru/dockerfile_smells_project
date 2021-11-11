FROM golang:1.8-alpine

RUN apk add --no-cache git

RUN go get github.com/go-sql-driver/mysql github.com/gorilla/securecookie golang.org/x/oauth2 golang.org/x/oauth2/google

COPY . /go/src/github.com/AscendTech4H/turtleauth

WORKDIR /go/src/github.com/AscendTech4H/turtleauth/server

RUN go build -o /bin/turtleauth

ENTRYPOINT ["turtleauth"]
