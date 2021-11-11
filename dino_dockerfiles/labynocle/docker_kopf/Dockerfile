FROM httpd:2.4-alpine

RUN apk add --no-cache git

ENV DIRPATH /usr/local/apache2/htdocs/

WORKDIR $DIRPATH

RUN rm *

RUN git clone git://github.com/lmenezes/elasticsearch-kopf.git kopf-v0.90

WORKDIR kopf-v0.90

RUN git checkout 1.0 \
        && cp -rp _site $DIRPATH/kopf-v1.x

RUN git checkout 2.0 \
        && cp -rp _site $DIRPATH/kopf-v2.x

RUN git checkout 0.90

COPY ./docroot/index.html /usr/local/apache2/htdocs/

RUN rm -rf .git/

EXPOSE 80
