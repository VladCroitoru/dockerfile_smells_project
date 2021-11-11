FROM python:2-alpine

RUN mkdir -p /src

WORKDIR /src
RUN apk add --no-cache nginx curl supervisor

COPY docker/supervisord.conf /etc/supervisord.conf
COPY docker/nginx-site.conf /etc/nginx/conf.d/default.conf
COPY docker/nginx.conf /etc/nginx/nginx.conf

# Bind annotator to all interfaces instead of just localhost
#ENV HOST=0.0.0.0

COPY annotator.cfg.docker annotator.cfg
COPY . /src
RUN pip install -e .[flask]

EXPOSE 80

CMD ["/usr/bin/supervisord", "-n", "-c",  "/etc/supervisord.conf"]
