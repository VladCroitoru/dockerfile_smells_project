FROM cmfatih/phantomjs
MAINTAINER daisuke nishimura 1.0 d@someonesgarden.org
RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y fonts-ipaexfont-gothic && \
  apt-get autoremove -y && \
  apt-get clean all

COPY bin/myRasterize.js /usr/bin/

ENTRYPOINT ["/usr/bin/phantomjs"]
CMD ["--help"]