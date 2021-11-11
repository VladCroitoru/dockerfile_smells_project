# e.g.: `docker build --rm --build-arg "NGINX_VERSION=1.14-alpine" -f ./Dockerfile .`
ARG NGINX_VERSION="latest"

FROM nginx:${NGINX_VERSION}

COPY --chown=nginx:nginx ./content/html /usr/share/nginx/html
COPY --chown=nginx:nginx ./content/html-errorpages /usr/share/nginx/html-errorpages
COPY --chown=nginx:nginx ./content/errorpages.conf /etc/nginx/errorpages.conf
COPY --chown=nginx:nginx ./content/default.conf /etc/nginx/conf.d/default.conf

RUN set -x \
    && nginx -v \
    && nginx -t
