FROM debian:buster-slim

ARG VIPS_VERSION=8.9.1
ARG VIPS_URL=https://github.com/libvips/libvips/releases/download
ARG VIPSHOME=/usr/local/vips

ENV PATH="${VIPSHOME}/bin:${PATH}"

COPY ./AptBuildTools /tmp/AptBuildTools
COPY ./AptImageProcessingTools /tmp/AptImageProcessingTools

RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive \
	apt-get install -y $(cat /tmp/AptBuildTools | xargs) $(cat /tmp/AptImageProcessingTools | xargs)

RUN echo 'Install mozjpeg' \
	&& cd /tmp \
    && git clone git://github.com/mozilla/mozjpeg.git \
    && cd /tmp/mozjpeg \
    && git checkout v3.3.1 \
    && autoreconf -fiv \
    && ./configure --prefix=/usr \
    && make install

RUN echo 'Build Lib Vips' \
	&& cd /tmp \
	&& wget ${VIPS_URL}/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.gz \
	&& tar zvxf vips-${VIPS_VERSION}.tar.gz \
	&& cd /tmp/vips-${VIPS_VERSION} \
	&& export PKG_CONFIG_PATH=${VIPSHOME}/lib/pkgconfig \
	&& ./configure --prefix=${VIPSHOME} --disable-gtk-doc --enable-debug=no --without-python \
	&& make \
	&& make install \
	&& ldconfig

# Clean the build area and make a tarball ready for packaging
RUN echo 'Cleaning up' \
	&& cd ${VIPSHOME} \
	&& rm bin/batch_* bin/vips-8.9 bin/vipsprofile bin/light_correct bin/shrink_width \
	&& strip lib/*.a lib/lib*.so* \
	&& rm -rf share/gtk-doc \
	&& rm -rf share/man \
	&& rm -rf share/thumbnailers \
	&& rm -rf /tmp/vips-${VIPS_VERSION}
	&& cd /usr/local \
	&& tar cfz libvips-dev.tar.gz vips

# Clean up
RUN echo 'Cleaning up build tools' \
	&& apt-get remove -y $(cat /tmp/AptBuildTools | xargs)
