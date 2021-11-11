FROM php:7.4.16-alpine

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

CMD [ "php", "--docroot", "public", "--server", "0.0.0.0:80", "/usr/src/app/common/router.php" ]
EXPOSE 80
HEALTHCHECK CMD wget --spider http://localhost || exit 1
VOLUME [ "/usr/src/app/config" ]
WORKDIR /usr/src/app

COPY [ "./src", "/usr/src/app/" ]
