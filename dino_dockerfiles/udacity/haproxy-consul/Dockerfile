FROM alpine:3.8

ADD install-haproxy.sh /tmp/install-haproxy.sh

RUN apk add --update curl && \
    # install deployed packages
    apk add libnl3 bash ca-certificates && \
    # install dumb-init
    curl -L -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 && \
    chmod +x /usr/local/bin/dumb-init && \
    # install haproxy
    /tmp/install-haproxy.sh && \
    # install consul-template 
    # NOTE: We use a patched version of 0.19.5 which removes some keys from the dedupe state to save disk space
    curl -L -o /usr/local/bin/consul-template https://github.com/udacity/consul-template/releases/download/v0.19.5-nochecks/consul-template && \
    chmod +x /usr/local/bin/consul-template && \
    # cleanup
    apk del curl && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /haproxy /consul-template/config.d /consul-template/template.d
ADD config/ /consul-template/config.d/
ADD template/ /consul-template/template.d/

ADD reload.sh /reload.sh
ADD launch.sh /launch.sh

CMD ["/launch.sh"]

### Udacity Image Metadata
COPY Dockerfile /Dockerfile

ARG udacity_name
ARG udacity_version
ARG udacity_git_url
ARG udacity_git_sha
ARG udacity_build_id
ARG udacity_build_timestamp
ARG udacity_build_origin

LABEL com.udacity.name="$udacity_name" \
      com.udacity.version="$udacity_version" \
      com.udacity.git.url="$udacity_git_url" \
      com.udacity.git.sha="$udacity_git_sha" \
      com.udacity.build.id="$udacity_build_id" \
      com.udacity.build.timestamp="$udacity_build_timestamp" \
      com.udacity.build.origin="$udacity_build_origin" \
      com.udacity.dockerfile="/Dockerfile" \
      com.udacity.api.packages="apk info -vv"
