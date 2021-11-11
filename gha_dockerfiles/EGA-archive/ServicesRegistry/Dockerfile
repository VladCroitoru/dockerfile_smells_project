##########################
## Build env
##########################
FROM python:buster AS BUILD

ENV DEBIAN_FRONTEND noninteractive

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update; \
#    apt-get upgrade -y; \
    apt-get install -y --no-install-recommends \
    ca-certificates pkg-config patch git gcc g++ make \
    bzip2 libssl-dev \
    ; \
#    rm -rf /var/lib/apt/lists/*; \
# python packages
    pip install --upgrade pip; \
    pip install -r /tmp/requirements.txt

##########################
## Final image
##########################
FROM python:buster

ARG COMMIT
ARG BUILD_DATE

LABEL maintainer "CRG System Developers"
LABEL org.label-schema.schema-version="0.1"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.vcs-url="https://github.com/EGA-archive/ServicesRegistry.git"
LABEL org.label-schema.vcs-ref=$COMMIT

# Too much ?
COPY --from=BUILD /usr/local      /usr/local

RUN apt-get update; \
#    apt-get upgrade -y; \
    apt-get install -y --no-install-recommends \
    ca-certificates nginx; \
    rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/nginx.list; \
    apt-get purge -y --auto-remove

COPY nginx.conf        /crg/nginx.conf
COPY supervisord.conf  /crg/supervisord.conf
COPY services_registry /crg/services_registry
COPY entrypoint.sh     /usr/local/bin/entrypoint.sh
COPY static/css        /crg/static/css
COPY static/img        /crg/static/img
COPY templates         /crg/templates

RUN groupadd crg                           && \
    useradd -M -g crg crg                  && \
#    mkdir /crg                             && \
    chown -R crg:crg /crg                  && \
    chown -R crg:crg /var/log/nginx        && \
    chown -R crg:crg /var/lib/nginx        && \
    chown -R crg:crg /etc/nginx            && \
    mkdir -p /var/run/crg                  && \
    chown -R crg:crg /var/run/crg          && \
    mkdir -p /var/log/crg                  && \
    chown -R crg:crg /var/log/crg          && \
    chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /crg
USER crg
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
