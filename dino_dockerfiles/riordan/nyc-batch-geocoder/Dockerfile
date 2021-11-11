FROM ubuntu:16.04

MAINTAINER David Riordan  <dr@daveriordan.com>
# Update, install unzip, curl, and nodejs
RUN apt-get update --yes && \
    apt-get upgrade --yes && \
    apt-get install --yes unzip curl nodejs npm && \
    ln -s `which nodejs` /usr/bin/node
    # ^ Fix Legacy naming nonsense on NodeJS/Ubuntu


WORKDIR  /nyc-batch-geocoder
# Download Geosupport Desktop for Linux
RUN curl -LOk http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gdelx_16d.zip && \
    unzip gdelx_16d.zip
RUN rm gdelx_16d.zip

# Set env variables to the full paths to lib/ and fls/
ENV LD_LIBRARY_PATH="/nyc-batch-geocoder/version-16d_16.4/lib/"
ENV GEOFILES="/nyc-batch-geocoder/version-16d_16.4/fls/"
#For within Node:  var lib = ffi.Library(...)
ENV GEOSUPPORT_LIBGEO="/nyc-batch-geocoder/version-16d_16.4/lib/libgeo.so"

ADD . /nyc-batch-geocoder/
RUN npm install

CMD ["node", "src/index.js"]
