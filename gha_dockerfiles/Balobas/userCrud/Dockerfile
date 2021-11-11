FROM golang:1.14
LABEL author="userCrud"
COPY . .
WORKDIR app
ENV GO111MODULE=on
ENV GOPATH=/app

COPY . .
EXPOSE 3000

CMD ["go", "run", "app/main.go"]
CMD ["go", "run", "app/testClient/main.go"]
