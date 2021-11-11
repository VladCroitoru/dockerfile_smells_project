FROM lancachenet/monolithic:latest
LABEL version=3
LABEL description="Single aggressive caching container for caching game content at LAN parties."
LABEL maintainer="LanCache.Net Team <team@lancache.net>"

ENV GENERICCACHE_VERSION=2 \    
	CACHE_MODE=generic \
    CACHE_MEM_SIZE=500m \
    CACHE_DISK_SIZE=1000000m \
    CACHE_MAX_AGE=3560d \
	CACHE_SLICE_SIZE=1m \
    UPSTREAM_DNS="8.8.8.8 8.8.4.4" \
    BEAT_TIME=1h \
    LOGFILE_RETENTION=3560 \
    NGINX_WORKER_PROCESSES=16

COPY overlay/ /

RUN rm -rf /data/cachedomains/*

VOLUME ["/data/logs", "/data/cache", "/var/www"]

EXPOSE 80 443

WORKDIR /scripts
