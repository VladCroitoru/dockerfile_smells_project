FROM alpine

RUN apk add --update nodejs \
 && rm /var/cache/apk/*

RUN npm install -g jsonlint \
 && npm install -g prettyjson

ENTRYPOINT ["jsonlint"]
CMD ["--help"]