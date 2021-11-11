# Pull base image.
FROM ubuntu:14.04

# Install GhostScript
ENV GHOSTSCRIPT_VERSION 9.02

RUN apt-get update -y \
&&  apt-get install -y \
	build-essential \
    gcc \
    make \
	curl \
    tar \
&&  apt-get clean all

RUN DIR=$(mktemp -d) \
    && cd ${DIR} \
    && curl -L -Os http://downloads.ghostscript.com/public/ghostscript-${GHOSTSCRIPT_VERSION}.tar.gz \
    && tar zxf ghostscript-${GHOSTSCRIPT_VERSION}.tar.gz \
    && cd ghostscript-${GHOSTSCRIPT_VERSION} \
    && ./configure --prefix="$SRC" --bindir="${SRC}/bin" \
    && make XCFLAGS=-DHAVE_SYS_TIME_H=1 \
    && make install \
    && make distclean \
    && rm -rf ${DIR}

# Install Java.
RUN \
  apt-get update && \
  apt-get install -y openjdk-7-jdk && \
  rm -rf /var/lib/apt/lists/*

# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

#Install ImageMagick
ENV IMAGEMAGICK_VERSION 6.7.8-10
ENV IMAGEMAGICK_ARCHIVE ImageMagick-$IMAGEMAGICK_VERSION.tar.gz
ENV IMAGEMAGICK_PREFIX /opt/ImageMagick
ENV IMAGEMAGICK_LD_CONF /etc/ld.so.conf.d/imagemagick.conf

RUN apt-get update -y \
&&  apt-get install -y \
	libc6-dev \
	libtiff4-dev \
	libpng-dev \
	libjpeg-dev \
&&  apt-get clean all

RUN mkdir -p $IMAGEMAGICK_PREFIX/src \
&& cd $IMAGEMAGICK_PREFIX/src \
&& curl -sL http://www.imagemagick.org/download/releases/$IMAGEMAGICK_ARCHIVE -o $IMAGEMAGICK_ARCHIVE \
&& tar xf $IMAGEMAGICK_ARCHIVE \
&& rm $IMAGEMAGICK_ARCHIVE \
&& cd ImageMagick-$IMAGEMAGICK_VERSION \
&& ./configure --prefix=$IMAGEMAGICK_PREFIX --enable-shared --disable-openmp --disable-opencl --without-x \
&& make \
&& make install \
&& rm -rf $IMAGEMAGICK_PREFIX/share \
&& rm -rf $IMAGEMAGICK_PREFIX/src

RUN echo $IMAGEMAGICK_PREFIX/lib/ > $IMAGEMAGICK_LD_CONF && ldconfig

ENV PATH /opt/ImageMagick/bin/:$PATH

ENV IMAGEMAGICK_PATH /opt/ImageMagick/bin

# Install Apache Tomcat

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \
	05AB33110949707C93A279E3D3EFE6B686867BA6 \
	07E48665A34DCAFAE522E5E6266191C37C037D42 \
	47309207D818FFD8DCD3F83F1931D684307A10A5 \
	541FBE7D8F78B25E055DDEE13C370389288584E7 \
	61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \
	79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \
	9BA44C2621385CB966EBA586F72C284D731FABEE \
	A27677289986DB50844682F8ACB77FC2E86E29AC \
	A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \
	DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \
	F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \
	F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23

ENV TOMCAT_MAJOR 8
ENV TOMCAT_VERSION 8.0.22
ENV TOMCAT_TGZ_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz

RUN set -x \
	&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \
	&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \
	&& gpg --verify tomcat.tar.gz.asc \
	&& tar -xvf tomcat.tar.gz --strip-components=1 \
	&& rm bin/*.bat \
	&& rm tomcat.tar.gz*

EXPOSE 8080:3389

CMD ["catalina.sh", "run"]
