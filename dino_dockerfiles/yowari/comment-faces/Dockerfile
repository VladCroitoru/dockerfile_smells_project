FROM centos

LABEL maintainer=yowari

RUN curl --silent --location https://rpm.nodesource.com/setup_9.x | bash - \
  && yum -y install nodejs gcc-c++ make wget

RUN wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo \
  && yum -y install yarn

RUN yum -y install ImageMagick

ENV GM_VERSION=1.3.28

RUN yum -y install libpng libjpeg libpng-devel libjpeg-devel ghostscript libtiff libtiff-devel freetype freetype-devel jasper jasper-devel \
  && cd /usr/src \
  && wget "ftp://ftp.graphicsmagick.org/pub/GraphicsMagick/1.3/GraphicsMagick-$GM_VERSION.tar.gz" \
  && tar -xzvf "GraphicsMagick-$GM_VERSION.tar.gz" \
  && cd "GraphicsMagick-$GM_VERSION" \
  && ./configure \
  && make install

RUN yum -y install bzip2

COPY . /opt/app-root
WORKDIR /opt/app-root

RUN yarn install \
  && yarn run build

RUN wget -E -H -p -k -e robots=off -P ranimes https://www.reddit.com/r/anime/wiki/commentfaces \
  && sed -i'.bak' 's/href="commentfaces.html#/href="#/g' ranimes/www.reddit.com/r/anime/wiki/commentfaces.html

RUN chmod -R 777 /opt/app-root \
  && chown -R 1001:1001 /opt/app-root

USER 1001

EXPOSE 8080

ENTRYPOINT ["yarn", "start"]
