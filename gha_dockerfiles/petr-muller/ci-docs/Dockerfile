FROM klakegg/hugo:0.75.1-ext-ubuntu as builder

COPY . /src/

RUN set -x && ln -s /bin/bash /usr/bin/bash && make generate

FROM nginxinc/nginx-unprivileged:1.18-alpine

COPY --from=builder /src/public/ /usr/share/nginx/html/
