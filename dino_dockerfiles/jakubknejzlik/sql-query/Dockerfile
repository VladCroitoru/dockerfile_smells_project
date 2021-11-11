FROM node:alpine

ENV CONNECTION_URL mysql://root:test@localhost/test
ENV QUERY query not specified

COPY . /code

WORKDIR /code

RUN npm install

ENTRYPOINT ["npm","start","--silent"]
