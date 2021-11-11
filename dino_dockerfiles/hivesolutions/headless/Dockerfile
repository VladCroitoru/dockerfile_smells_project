FROM hivesolutions/ubuntu_dev:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 8080

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 8080
ENV NODE_ENV production

ADD app.js /app/
ADD package.json /app/
ADD lib /app/lib

WORKDIR /app

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y bzip2 fontconfig\
    libpangocairo-1.0-0 nodejs
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y gconf-service\
    libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1\
    libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0\
    libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6\
    libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1\
    libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6\
    libgbm-dev ca-certificates fonts-liberation fonts-emojione libappindicator1\
    libnss3 lsb-release xdg-utils wget
RUN npm install

CMD ["/usr/bin/node", "/app/app.js"]
