FROM golang

ADD . /go/src/github.com/tesis-lab/tesis

RUN apt-get update

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

RUN npm install webpack -g


WORKDIR /go/src/github.com/tesis-lab/tesis
RUN npm config set registry http://registry.npmjs.org/ && npm install


RUN go get github.com/dchest/uniuri
RUN go get github.com/gorilla/mux
RUN go get github.com/gorilla/websocket
RUN go install github.com/tesis-lab/tesis/editor

RUN webpack

# Run the server command by default when the container starts.
ENTRYPOINT /go/bin/editor

# Document that the service listens on port 8000.
EXPOSE 8000
