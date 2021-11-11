FROM node:latest

RUN git clone --depth 1 https://github.com/cure53/Flashbang /usr/local/src/flashbang
COPY index.html /usr/local/src/flashbang/index.html
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    openjdk-7-jre \
    unzip \
  && npm install -g \
    grunt-cli \
    http-server \
  && cd /usr/local/src/flashbang/shumway \
  && git submodule init \
  && make bootstrap \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/*

EXPOSE 80
WORKDIR /usr/local/src/flashbang
CMD ["http-server", "-p", "80", "-d", "False", "."]
