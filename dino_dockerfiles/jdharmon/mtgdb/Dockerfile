FROM alpine AS build
RUN apk --no-cache add curl jq mongodb-tools zip
WORKDIR /tmp/data
RUN curl -sO https://mtgjson.com/json/AllSets.json.zip \
 && unzip AllSets.json.zip \
 && mkdir /data \
 && jq -r 'to_entries[] | .value | del(.cards)' AllSets.json > /data/sets.json \
 && jq -r 'to_entries[] | .value.cards[] + {set: .key}' AllSets.json > /data/cards.json
 
FROM alpine
RUN apk --no-cache add mongodb libsasl
COPY --from=build /usr/bin/mongoimport /usr/bin
COPY --from=build /data /data
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
VOLUME /data/db
EXPOSE 27017
CMD docker-entrypoint.sh