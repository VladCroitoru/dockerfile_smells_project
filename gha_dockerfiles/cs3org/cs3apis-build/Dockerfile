# Docker file to build the cs3apis
# To push locally:
# docker build .
# docker tag xxxx cs3org/cs3apis:latest
# docker push cs3org/cs3apis
FROM golang
RUN apt-get update
RUN apt-get install build-essential curl unzip sudo -y
RUN apt-get install python3-pip -y

# deps for protoc
RUN cd /tmp && curl -sSL https://github.com/protocolbuffers/protobuf/releases/download/v3.9.2/protoc-3.9.2-linux-x86_64.zip -o protoc.zip && unzip -o protoc.zip && sudo cp bin/protoc /usr/local/bin/protoc
RUN cd /tmp && curl -sSL https://github.com/uber/prototool/releases/download/v1.10.0/prototool-Linux-x86_64 -o prototool && sudo cp prototool /usr/local/bin/ && sudo chmod u+x /usr/local/bin/prototool
RUN cd /tmp && curl -sSL https://github.com/nilslice/protolock/releases/download/v0.14.1/protolock.20190917T024843Z.linux-amd64.tgz -o protolock.tgz && tar -xzf protolock.tgz && sudo cp protolock /usr/local/bin/
RUN curl -sSL https://github.com/pseudomuto/protoc-gen-doc/releases/download/v1.3.0/protoc-gen-doc-1.3.0.linux-amd64.go1.11.2.tar.gz -o protoc-gen-doc.tar.gz && tar xzfv protoc-gen-doc.tar.gz && sudo cp protoc-gen-doc-*/protoc-gen-doc /usr/local/bin/
RUN go install github.com/golang/protobuf/protoc-gen-go@v1.3.2

# deps for python
RUN sudo python3 -m pip install grpcio grpcio-tools --ignore-installed

# deps for js
RUN curl -sSL https://github.com/grpc/grpc-web/releases/download/1.0.6/protoc-gen-grpc-web-1.0.6-linux-x86_64 -o /tmp/protoc-gen-grpc-web
RUN sudo mv /tmp/protoc-gen-grpc-web /usr/local/bin/ && sudo chmod u+x /usr/local/bin/protoc-gen-grpc-web

# deps for node.js
RUN curl -fsSL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g grpc-tools

# compile build tool and put it into path
ADD . /root/cs3apis-build
RUN cd /root/cs3apis-build/ && go build . &&  sudo cp cs3apis-build /usr/local/bin && sudo chmod u+x cs3apis-build

WORKDIR /root/cs3apis
