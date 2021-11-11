FROM node:4

RUN git config --global user.name uptocode \
    && git config --global user.email uptocode@porch.com \
    && git config --global push.default simple

RUN npm install -g npm@3.10.5

WORKDIR /opt/build
COPY package.json /opt/build/
RUN npm install --production

COPY . /opt/build/

ENTRYPOINT ["node", "bin/index.js"]
