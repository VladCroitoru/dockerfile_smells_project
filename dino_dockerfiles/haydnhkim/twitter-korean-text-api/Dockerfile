FROM openjdk:8-jdk-alpine

RUN apk add --update --no-cache nodejs python make g++ && \
  python -m ensurepip && \
  rm -r /usr/lib/python*/ensurepip && \
  pip install --upgrade pip setuptools && \
  rm -r /root/.cache

# Replace shell with bash so we can source files
# RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Fix bug https://github.com/npm/npm/issues/9863
RUN cd $(npm root -g)/npm \
  && npm install fs-extra \
  && sed -i -e s/graceful-fs/fs-extra/ -e s/fs\.rename/fs.move/ ./lib/utils/rename.js

WORKDIR /usr/src/myapp
COPY . /usr/src/myapp

RUN npm install -g pm2 \
  && cd /usr/src/myapp \
  && npm install java \
  && npm install

EXPOSE 3000
CMD ["pm2-docker", "index.js"]
