FROM gerasim13/golang
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>

RUN /bin/bash go-wrapper download github.com/compose/transporter/...
RUN /bin/bash go-wrapper install github.com/compose/transporter/...

WORKDIR /rest
ADD ./rest.go /rest/main.go
RUN go get github.com/ant0ine/go-json-rest/rest
RUN go build -o main .

ENV CONFIG '/app/config.yaml'
ENV APP '/app/application.js'

WORKDIR /app
VOLUME ["/app"]

EXPOSE 8080
CMD ["/rest/main"]
