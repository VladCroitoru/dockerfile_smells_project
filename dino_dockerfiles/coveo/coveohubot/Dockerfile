FROM buildpack-deps:jessie

ENV PORT 8080
EXPOSE 8080

RUN curl -SLO "https://iojs.org/dist/v3.2.0/iojs-v3.2.0-linux-x64.tar.gz" \
  && tar -xzf "iojs-v3.2.0-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "iojs-v3.2.0-linux-x64.tar.gz"

RUN useradd -d /hubot -m -s /bin/bash -U hubot
WORKDIR /hubot

COPY . /hubot

RUN npm install

ENTRYPOINT ["/hubot/bin/hubot"]
