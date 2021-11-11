FROM node:6.2.0

WORKDIR /opt

RUN apt-get update && \
  apt-get install -y  \
  libgconf2-4 libxtst6 libnss3 libasound2 xvfb dbus-x11 libgtk2.0-common libnotify4 \
  xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic fonts-font-awesome fonts-takao-mincho && \
  rm -rf /var/lib/apt/lists/*

RUN npm install -g electron-prebuilt@0.30.5

COPY ./package.json /opt/package.json
RUN npm install --production

COPY ./run.sh /opt/run.sh
COPY ./lib/ /opt/lib/

CMD [ "sh", "/opt/run.sh" ]
