FROM golang:1.8
WORKDIR /app
ENV MYSQL_CONNECTION=user:password@tcp(sonar.paas.sbtech.com:3306)/build?charset=utf8
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/gc_cloud.json
EXPOSE 8080
VOLUME ["/var/cfg"]
COPY . /app
RUN mkdir -p /var/cfg
RUN go get github.com/go-sql-driver/mysql
RUN go get github.com/go-xorm/xorm
RUN go get github.com/gorilla/mux
RUN go get github.com/rs/cors
RUN go get golang.org/x/net/context
RUN go get golang.org/x/oauth2/google
RUN go get google.golang.org/api/compute/v1
RUN cd /app; go build -o myapp;
ENTRYPOINT ["./myapp"]