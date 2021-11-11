FROM golang:1.8

ARG app_env
ENV APP_ENV $app_env

ENV SRC_DIR=/go/src/github.com/janisgarklavs/tournament/

ADD . $SRC_DIR
WORKDIR $SRC_DIR

RUN go get -t 
RUN go build -o app

CMD if [ ${APP_ENV} = production ]; \
    then \
    ./app; \
    else \
    go get github.com/pilu/fresh && \
    fresh; \
    fi
EXPOSE 8080