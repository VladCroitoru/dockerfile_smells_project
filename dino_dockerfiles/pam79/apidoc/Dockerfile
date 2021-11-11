FROM node:8.9.4-alpine

MAINTAINER Abdullah Morgan <paapaabdullahm@gmail.com>

ENV DOC_INPUT=./
ENV DOC_OUTPUT=docs/

RUN npm install apidoc -g;

WORKDIR /app

CMD [ "apidoc", "-i", "${DOC_INPUT}", "-o", "${DOC_OUTPUT}" ]
