FROM node:12

# アプリのディレクトリ
WORKDIR /app

COPY package*.json ./

# node_module インストール
RUN npm install

# DockerfileのあるディレクトリからWORKDIRへコピー
COPY ./blog-app/ .
RUN chmod 755 ./start.sh
EXPOSE 3000

CMD ["./start.sh" ]
