FROM memcached:1.5.12
USER root
RUN apt-get update && apt-get install -y netcat && apt-get clean
USER memcache
HEALTHCHECK --start-period=3s --timeout=2s --interval=10s CMD ["/bin/nc","-z","127.0.0.1","11211"]
