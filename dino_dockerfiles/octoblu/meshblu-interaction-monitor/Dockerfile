FROM nginx:alpine
MAINTAINER Octoblu <docker@octoblu.com>

HEALTHCHECK CMD curl --fail http://localhost:80/healthcheck || exit 1

WORKDIR /opt/app

RUN apk add --no-cache \
  bash \
  ca-certificates \
  curl

COPY . .

RUN cat package.json \
      | grep version \
      | head -1 \
      | awk -F: '{ print $2 }' \
      | sed 's/[",]//g' \
      | tr -d '[[:space:]]' > .PKG_VERSION

RUN sed -e \
  "s/PKG_VERSION/$(cat .PKG_VERSION)/" \
  ./templates/default.template > \
  /etc/nginx/conf.d/default.conf

RUN cp ./templates/*.conf /etc/nginx/conf.d/

CMD [ "./scripts/run-nginx.sh" ]
