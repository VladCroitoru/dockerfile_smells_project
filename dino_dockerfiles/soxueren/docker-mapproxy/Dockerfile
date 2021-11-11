#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
FROM yagajs/mapproxy:1.11-alpine
MAINTAINER jxw<jxw@jxw>

ADD app.py /mapproxy/
ADD epsg /mapproxy/
ADD mapproxy.yaml /mapproxy/

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["mapproxy"]

USER mapproxy
VOLUME ["/mapproxy"]

EXPOSE 8080
# Stats
EXPOSE 9191
