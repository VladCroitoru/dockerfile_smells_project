FROM node:latest

WORKDIR /usr/src/
ENV HOME /usr/src/

RUN mkdir -p /usr/src/
COPY . /usr/src/

RUN npm install -g forever bower gulp-cli
RUN npm install
RUN make

CMD [ "forever", "app.js" ]
