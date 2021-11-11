FROM debian

MAINTAINER Rafal S. <rafal@maracje.pl>

ENV DEBIAN_FRONTEND noninteractive
ENV VERSION phantomjs-2.1.1-linux-x86_64

RUN apt-get update && apt-get -y install openssl tar curl fontconfig libfreetype6 bzip2 && \
mkdir /e && \
curl -SL https://bitbucket.org/ariya/phantomjs/downloads/${VERSION}.tar.bz2 | tar xj && \
curl -SL https://raw.githubusercontent.com/ariya/phantomjs/master/examples/rasterize.js -o /e/rasterize-latest.js && \
ln -s /${VERSION}/bin/phantomjs /bin/phantomjs && \
mv -v ${VERSION}/examples/* /e/ && \
rm -rf -- /var/lib/apt/* /var/log/*

VOLUME ["/img"]
WORKDIR /img

CMD /bin/phantomjs
