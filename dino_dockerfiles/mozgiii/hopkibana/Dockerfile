FROM node

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install

COPY bin/* /usr/local/bin/

CMD [ "echo", "Use `export` or `import` commands please." ]
