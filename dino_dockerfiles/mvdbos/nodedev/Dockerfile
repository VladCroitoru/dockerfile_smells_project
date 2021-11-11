from node:latest

MAINTAINER Matthijs van den Bos <matthijs@vandenbos.org>

ENV TARGET_DIR="/usr/local/lib/nodedev"

RUN mkdir -p $TARGET_DIR

WORKDIR $TARGET_DIR

COPY usage.txt $TARGET_DIR

RUN npm install -g grunt-cli grunt-init nodemon

CMD cat $TARGET_DIR/usage.txt
