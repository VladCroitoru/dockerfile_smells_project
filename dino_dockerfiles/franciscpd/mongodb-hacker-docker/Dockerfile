FROM mongo:latest
MAINTAINER FrancisCPD <franciscpd@gmail.com>

RUN apt-get update \
 && apt-get install -y git \
 && apt-get install -y build-essential \
 && git clone --depth=1 https://github.com/TylerBrock/mongo-hacker.git \
 && rm -rf ~/.mongorc.js \
 && cd mongo-hacker \
 && make install

CMD ["mongod"]
