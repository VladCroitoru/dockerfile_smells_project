FROM golang:1.5
MAINTAINER Helena Rasche <hxr@hx42.org>
EXPOSE 80

ENV GIT_REV 93018954e78f7afc2157de9c4df7cc24afc1f333

RUN wget https://github.com/erasche/barcode-server/archive/${GIT_REV}.tar.gz && \
    tar xvfz ${GIT_REV}.tar.gz && \
    mv barcode-server-${GIT_REV}/ /app/ && \
    go get -v github.com/codegangsta/cli && \
    go get -v github.com/boombuler/barcode && \
    go get -v github.com/gorilla/mux && \
    go get -v github.com/gorilla/handlers

CMD ["go", "run", "/app/main.go", "-l", "0.0.0.0:80"]

