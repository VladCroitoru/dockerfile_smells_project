FROM postgres:9.4-alpine
MAINTAINER thimico

RUN apk update
RUN apk upgrade

RUN apk add tzdata

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]