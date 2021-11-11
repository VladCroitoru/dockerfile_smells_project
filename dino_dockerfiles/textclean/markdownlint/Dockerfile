FROM textclean/node-base
MAINTAINER nickg
WORKDIR /tmp
RUN /bin/true \
  && npm install -g markdownlint-cli@0.2.0 \
  && npm cache clean
USER daemon
ENTRYPOINT [ "/usr/bin/markdownlint" ]
