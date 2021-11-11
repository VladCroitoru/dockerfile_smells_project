FROM ubuntu:latest

WORKDIR /shapefiles
ADD https://gist.githubusercontent.com/diegovalle/5843688/raw/76a6f17f0a0c3007491934efa2ae3b1f74934f7d/download-census-shp.sh /shapefiles/download.sh

RUN chmod +x /shapefiles/download.sh
RUN apt-get -y update && apt-get install software-properties-common -y
RUN add-apt-repository ppa:arx/release && apt-get update &&\
    apt-get install innoextract -y
RUN apt-get install -y curl gdal-bin libgdal-dev
# Create the directory for downloading the shapefiles
RUN mkdir -p /shapefiles/shps &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["/bin/bash"]
