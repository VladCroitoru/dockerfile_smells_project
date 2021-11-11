# Node.js version for Kibana 4.5.0
FROM mhart/alpine-node:4.3.0
MAINTAINER Serandel <serandel@gmail.com>

EXPOSE 5601

RUN apk update && apk add git python make g++ && rm -rf /var/cache/apk/*
RUN git clone --branch v4.5.0 https://github.com/elastic/kibana.git kibana 

WORKDIR /kibana

# Sorry, Mario, Elasticsearch is in another castle!
RUN printf '\nelasticsearch.url: "http://elasticsearch:9200"\n' >> config/kibana.yml

# Bug with "loader-utils" NPM transitive dependency, we have to pin a correct version
# https://github.com/elastic/kibana/pull/6887/files
RUN sed -i 's/"lodash"/"loader-utils": "0.2.12",\n    "lodash"/' package.json

RUN npm install

CMD npm start