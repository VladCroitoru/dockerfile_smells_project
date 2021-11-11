FROM golang:1.8.3

RUN apt-get update && apt-get install -y git unzip

RUN wget https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip \
&& unzip protoc-3.3.0-linux-x86_64.zip -d protoc
RUN cp protoc/bin/protoc ./bin/protoc

RUN go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
RUN go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
RUN go get -u github.com/golang/protobuf/protoc-gen-go

RUN mkdir /protoc_dir

COPY ./generate.sh .

CMD ["bash", "-c", "/go/generate.sh"]
