##
# Create the fatmap/mapserver Docker image.
#

FROM fatmap/gdal:2.3-dev

MAINTAINER FATMAP Platform Team <platform@fatmap.com>

# Build the image.
COPY . /tmp/
RUN /tmp/build.sh

VOLUME /maps

EXPOSE 9005

CMD /usr/bin/spawn-fcgi -n -a 0.0.0.0 -p 9005 -- /usr/bin/multiwatch -f 1 -- /usr/local/bin/mapserv
