FROM node:14.15.1

# imageの説明
LABEL version="0.0.1"
LABEL description="graphql api for twitter-clone"
LABEL maintainer="persona product"


# 環境変数
# - 本番環境用
# ENV NODE_ENV=production
# - 開発環境用（composeファイルに記述済）
# ENV NODE_ENV=development
# ENV PORT=4000
# ENV DATABASE_URL=postgres://root:password@postgres:5432/twitter_clone


# コンテナ内の作業ディレクトリ
WORKDIR /app

# ホストマシンからコンテナへファイルコピー
COPY package.json yarn.lock ./
# ./で書いても同じ
# COPY package.json yarn.lock /app


RUN yarn
# package.json yarn.lockを素に、ホストの環境と同じパッケージをインストール


COPY . .
# ホストマシンのディレクトリを、コンテナ内の/appへバンドル


EXPOSE 4000
# ポート番号の指定


# 起動コマンド
CMD [ "yarn", "start:dev" ]


# ーーーーーーーーーーーーーーーーー
# コンテナ内に接続するコマンド
# docker ps で <container id> を取得
# docker exec -it <container id> /bin/bash











