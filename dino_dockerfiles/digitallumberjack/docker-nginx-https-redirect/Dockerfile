FROM nginx:1.11
MAINTAINER digitalLumberjack <digitallumberjack@gmail.com>

ENV HOST '$host'

COPY ./default.conf /etc/nginx/conf.d/default.template

CMD /bin/bash -c "envsubst '\$HOST' < /etc/nginx/conf.d/default.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"
