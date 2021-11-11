FROM golang:latest

RUN mkdir /go/src/work

WORKDIR /go/src/work

COPY . /go/src/work

# RUN  go mod init example.com/hello  \ 
# && go get github.com/lib/pq
# ポートを開ける
EXPOSE 8081

# デフォルトコマンド
CMD ["/bin/bash"]