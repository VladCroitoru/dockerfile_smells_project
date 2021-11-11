FROM wernight/phantomjs:latest

# switch to root
USER root
RUN apt-get update \
    && apt-get install -y git-core npm \
    && apt-get clean \
    && cd /home/phantomjs \
    && mkdir wavedrom-cli \
    && git clone https://github.com/wavedrom/cli.git \
       /home/phantomjs/wavedrom-cli \
    && npm install wavedrom-cli --save-dev \
    && mkdir /data
# USER phantomjs
# switch back to default user

VOLUME ["/data"]
WORKDIR /data

ENTRYPOINT ["phantomjs", "/home/phantomjs/node_modules/wavedrom-cli/bin/wavedrom-cli.js"]

