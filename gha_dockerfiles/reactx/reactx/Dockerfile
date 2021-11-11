FROM node:10

ADD yarn.lock /yarn.lock

ENV NODE_PATH=/node_modules
ENV PATH=$PATH:/node_modules/.bin
RUN yarn

WORKDIR /app
ADD . /app

ENTRYPOINT ["/bin/bash", "/app/run.sh"]
CMD ["build"]