# BOOSTER-WEB docker file

FROM nginx:1.17.9

# File Author / Maintainer
LABEL maintainer=frederic.lemoine@pasteur.fr

COPY . /gopath/src/github.com/evolbioinfo/booster-web
COPY docker/booster-web.toml.template /home/booster/booster-web.toml.template
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

# Build booster-web
ENV PATH=/usr/local/go/bin:/gopath/bin/:$PATH
ENV GOPATH=/gopath

USER root

RUN apt-get update --fix-missing && apt-get install -y curl git gcc \
    && curl -k https://storage.googleapis.com/golang/go1.16.4.linux-amd64.tar.gz > /usr/local/go1.16.4.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf /usr/local/go1.16.4.linux-amd64.tar.gz \
    && rm -f /usr/local/go1.16.4.linux-amd64.tar.gz \
    && mkdir -p /gopath/ \
    && cd /gopath/src/github.com/evolbioinfo/booster-web \
    && go get github.com/go-bindata/go-bindata/...@v3.1.2 \
    && go get github.com/elazarl/go-bindata-assetfs/...@v1.0.0 \
    && go-bindata-assetfs -pkg static  webapp/static/... \
    && mv bindata_assetfs.go static \
    && go-bindata -o bindata_templates.go -pkg templates  webapp/templates/... \
    && mv bindata_templates.go templates \
    && go get . \
    && go build -o booster-web -ldflags "-X github.com/evolbioinfo/booster-web/cmd.Version=v1.8" github.com/evolbioinfo/booster-web \
    && mv booster-web /home/booster/booster-web \
    && rm -rf /gopath /usr/local/go

RUN chown -R nginx:nginx /var/cache/nginx && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d

RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid

RUN chmod 777 /home/booster
RUN chown nginx /var/cache/nginx/

COPY docker/startup.sh /home/booster/startup.sh
RUN chmod 777 /home/booster/startup.sh

USER nginx

ENTRYPOINT ["bash","/home/booster/startup.sh"]
