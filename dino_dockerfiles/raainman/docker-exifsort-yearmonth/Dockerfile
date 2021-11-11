FROM ubuntu:16.04

LABEL maintainer "Raymond Koppen" \
      email="raymond.koppen@gmail.com"

RUN apt-get update \
  && apt-get install -y imagemagick file \
  && apt-get clean \
  && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

COPY exifsort.sh /usr/local/bin/exifsort.sh

RUN chmod +x /usr/local/bin/exifsort.sh

ENV TS_AS_FILENAME=TRUE USE_LMDATE=TRUE USE_FILE_EXT=TRUE JPEG_TO_JPG=FALSE
ENV FILETYPES "*.jpg" "*.jpeg"

WORKDIR /var/photo

CMD /usr/local/bin/exifsort.sh /var/photo

