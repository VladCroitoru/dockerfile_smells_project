FROM node:6-slim

MAINTAINER Tobias Gurtzick <magic@wizartales.com>

WORKDIR /home/node
USER node

RUN npm install sinopia && npm install js-yaml rc

Add config.yaml .
ADD configure.js .
ADD start.sh .

CMD ["./start.sh"]
EXPOSE 4873
VOLUME /home/node
