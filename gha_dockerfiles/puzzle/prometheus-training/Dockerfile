FROM klakegg/hugo:0.88.0-ext-ubuntu AS builder

ARG ACEND_HUGO_ENV=default

COPY . /src

RUN hugo --environment ${ACEND_HUGO_ENV} --minify

FROM nginxinc/nginx-unprivileged:1.21-alpine

# prevent nginx from adding ports in redirects
USER root
RUN sed -i '/^http {/a \    port_in_redirect off;' /etc/nginx/nginx.conf
USER 101

COPY --from=builder /src/public /usr/share/nginx/html
