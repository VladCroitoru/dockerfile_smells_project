FROM node:slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install
COPY . /usr/src/app

RUN mkdir -p /data
VOLUME /data
WORKDIR /data

ENV PATH /usr/src/app/bin:$PATH
ENTRYPOINT ["/usr/src/app/bin/raml1-doc.js"]

CMD ["--help"]
