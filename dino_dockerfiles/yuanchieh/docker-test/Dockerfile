FROM ubuntu:14.04
RUN apt-get update && apt-get install -y nginx curl && curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash - && apt-get install -y nodejs
COPY test /test

CMD node /test/test.js
