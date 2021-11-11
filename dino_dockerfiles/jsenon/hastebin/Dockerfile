FROM node
LABEL version="1.2"
LABEL description="Haste is the prettiest, easiest to use pastebin ever made"
LABEL maintainer="julien.senon@gmail.com"



RUN git clone https://github.com/seejohnrun/haste-server.git /opt/haste
WORKDIR /opt/haste

RUN rm /opt/haste/about.md
ADD conf/about.MD /opt/haste/

RUN npm install

ADD conf/config.js /opt/haste/config.js

VOLUME ["/opt/haste/data"]

EXPOSE 7777
CMD ["npm", "start"]
