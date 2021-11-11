FROM node:8-alpine

ENV SOURCE_URL mysql://root:test@localhost/test
ENV SOURCE_QUERY "SELECT * FROM table"
ENV DESTINATION_URL mysql://root:test@localhost/test
ENV DESTINATION_TABLE table_name

COPY . /code

WORKDIR /code

RUN npm install

ENTRYPOINT ["npm","start","--silent"]
