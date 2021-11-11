# ベースイメージ作成。(現在の最新バージョン)
FROM golang:1.16.7

#vimを利用するため。
RUN apt-get update && apt-get -y install vim

# プロジェクト用のディレクトリを作成する。
RUN mkdir -p /go/src/optim_22_app/

# typefile packageのためのディレクトリを作成する。
RUN mkdir -p /usr/local/go/src/typefile/

# type.goファイルを作成する
RUN touch /usr/local/go/src/typefile/type.go

# ホストのtype.goの内容をコピーする
COPY ./typefile/type.go /usr/local/go/src/typefile/type.go

# カレントディレクトリの内容をコピーする
COPY . /go/src/optim_22_app/

# コンテナ内で各種命令を実行するためのカレントディレクトリを指定
WORKDIR /go/src/optim_22_app/

# モジュールモードのためにライブラリをインストールする
RUN go mod download

# イメージを実行する時、コンテナに対して何もオプションを指定しなければ、
# 自動的に実行するコマンドを CMD 命令で指定
CMD ["go","run","/go/src/optim_22_app/main.go"]