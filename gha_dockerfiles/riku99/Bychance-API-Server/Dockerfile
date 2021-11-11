FROM node:12
RUN apt-get update \
    && apt-get install -y ffmpeg
WORKDIR /app
COPY package*.json /app
RUN yarn install
COPY . /app
# 以下2行は ‘darwin-x64’ binaries cannot be used on the ‘linux-x64’ platform. に対応するため。もしダメならコンテナ内に入ってみる
RUN rm -rf node_modules/sharp
RUN yarn add --arch=x64 --platform=linux sharp
RUN chmod 744 ./start.sh
CMD ["./start.sh"]