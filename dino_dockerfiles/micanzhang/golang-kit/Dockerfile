FROM micanzhang/golang-testing:latest

# build protoc
ADD build-protoc.sh build-protoc.sh
RUN /bin/sh build-protoc.sh && rm build-protoc.sh

# golang protobuf plugin
# https://github.com/golang/protobuf/blob/master/README.md
# Versions v1.4 and later of github.com/golang/protobuf are implemented in terms of google.golang.org/protobuf.
# Programs which use both modules must use at least version v1.4 of this one.
RUN GO111MODULE=on go get github.com/golang/protobuf/protoc-gen-go@v1.3.5

# install python3
RUN apt-get install -y python3 python3-pip && \
    pip3 install --upgrade pip setuptools && \
    if [[ ! -e /usr/bin/pip ]]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
