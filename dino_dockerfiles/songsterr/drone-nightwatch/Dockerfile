FROM node:8.10.0-alpine

RUN apk --no-cache add git python \
 && yarn global add nightwatch \
 && mkdir -p /test/

ADD nightwatch.reporter.js /test/
ADD script.sh /bin/

RUN chmod +x /bin/script.sh
ENTRYPOINT /bin/script.sh
