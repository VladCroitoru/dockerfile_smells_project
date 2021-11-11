FROM alpine

RUN apk add --no-cache bash

RUN mkdir /script \
&&  wget -O /script/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
&&  chmod +x /script/wait-for-it.sh

ENTRYPOINT ["/script/wait-for-it.sh"]
