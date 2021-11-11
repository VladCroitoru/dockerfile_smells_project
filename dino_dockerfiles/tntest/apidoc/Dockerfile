FROM node:0.12
MAINTAINER TNTest

# Install apidoc.
RUN npm install apidoc@0.13 -g

# template
COPY template /template

ENV CONF_DIR /usr/app
ENV SRC_DIR /usr/app/src

RUN mkdir -p $SRC_DIR
RUN mkdir -p $CONF_DIR

CMD apidoc -i $SRC_DIR -o /out -t /template -c $CONF_DIR
