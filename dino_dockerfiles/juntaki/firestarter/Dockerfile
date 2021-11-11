FROM golang:1.10.0-stretch
ENV SRC_DIR=/go/src/github.com/juntaki/firestarter
ADD . $SRC_DIR
WORKDIR $SRC_DIR

RUN cd $SRC_DIR && \
    go get -u -v && \
    go build -o main .


FROM node:9.6.1
ENV SRC_DIR=/go/src/github.com/juntaki/firestarter
ADD . $SRC_DIR
WORKDIR $SRC_DIR

RUN cd $SRC_DIR/admin && \
    yarn install && \
    yarn build


FROM golang:1.10.0-stretch
ENV SRC_DIR=/go/src/github.com/juntaki/firestarter

COPY --from=0 $SRC_DIR/main /app/main
COPY --from=0 $SRC_DIR/swagger-ui /app/swagger-ui
COPY --from=1 $SRC_DIR/admin/dist /app/admin/dist
WORKDIR /app

EXPOSE 3000
EXPOSE 8080
CMD ["/app/main"]