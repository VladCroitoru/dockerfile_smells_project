FROM hbthlw/node-ubuntu:2.3

RUN apt-get install -y \
  libcairo2-dev \
  libjpeg8-dev \
  libpango1.0-dev \
  libgif-dev \
  build-essential \
  g++ \
  gcc

RUN mkdir -p /usr/share/fonts/userfonts/
COPY ./PingFang_Regular.otf /usr/share/fonts/userfonts/

RUN fc-list :lang=zh

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN npm install pm2 -g

EXPOSE 3000
VOLUME ["/usr/src/app"]

CMD ["npm", "start"]

