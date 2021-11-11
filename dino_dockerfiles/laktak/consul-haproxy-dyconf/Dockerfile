FROM alpine
MAINTAINER Christian Zangl, http://github.com/laktak/

EXPOSE 80 1936

# install node & haproxy
RUN apk --update add nodejs-npm haproxy

COPY config.hjson controller.js package.json /app/

# install dyconf & dependencies
RUN npm i dyconf@1.1.0 -g && cd /app && npm i

ENTRYPOINT ["/usr/bin/dyconf", "-config=/app/config.hjson"]
