FROM mkenney/npm

RUN cd / \
  && git clone https://github.com/kenperlin/chalktalk.git --depth=1 \
  && cd ./chalktalk/server/ \
  && npm install

WORKDIR /chalktalk
CMD node server/main.js
