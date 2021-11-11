FROM debian

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
ENV NVM_DIR /root/.nvm
ENV IOJS_VERSION 2.1.0

RUN apt-get update \
  && apt-get install -y curl \
  && curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.25.3/install.sh | bash \
  && source $NVM_DIR/nvm.sh \ 
  && nvm install iojs-v$IOJS_VERSION \
  && nvm alias default iojs-v$IOJS_VERSION \
  && nvm use default

ENV NODE_PATH $NVM_DIR/versions/io.js/v$IOJS_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/io.js/v$IOJS_VERSION/bin:$PATH

CMD [ "node" ]

