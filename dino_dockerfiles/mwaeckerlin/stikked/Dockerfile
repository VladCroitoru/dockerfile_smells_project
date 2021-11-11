FROM ubuntu
MAINTAINER mwaeckerlin
ENV TERM xterm

ENV SOURCE_URL="https://github.com"
ENV SOURCE_PATH="/claudehohl/Stikked"

RUN apt-get install -y wget
WORKDIR /tmp
RUN export VERSION=$(wget -O- -q ${SOURCE_URL}${SOURCE_PATH}/tags \
                     | sed -n 's,.*href="'${SOURCE_PATH}'/archive/\(.*\)\.tar\.gz".*,\1,p;Tc;q;:c'); \
    wget -q ${SOURCE_URL}${SOURCE_PATH}/archive/${VERSION}.tar.gz; \
    tar xf ${VERSION}.tar.gz; \
    mv Stikked-${VERSION}/htdocs /stikked; \
    rm ${VERSION}.tar.gz; \
    rm -r Stikked-${VERSION}
WORKDIR /stikked
RUN mkdir -p /usr/share/nginx
RUN ln -s /stikked /usr/share/nginx/html
ADD start.sh /start.sh
ADD nginx.conf /etc/nginx/sites-enabled/stikker
CMD /start.sh

VOLUME /stikked
VOLUME /usr/share/nginx/html
VOLUME /etc/nginx/sites-enabled
