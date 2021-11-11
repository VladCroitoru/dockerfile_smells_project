#++++++++++++++++++++++++++++++++++++++++++++#
#      XunSearch Docker container in Centos  #
#++++++++++++++++++++++++++++++++++++++++++++#

FROM centos
MAINTAINER limingxinleo<m@glad.so>

ENV XS_VERSION=1.4.9 \
    XS_PREFIX=/opt/xunsearch \
    XS_DATA=/opt/xunsearch/data

# Install required packages
RUN yum -y install bzip2 gcc gcc-c++ wget automake autoconf libtool make zlib-devel

# Download Xunsearch
RUN wget http://www.xunsearch.com/download/xunsearch-full/xunsearch-full-$XS_VERSION.tar.bz2 \
    && tar -xjf xunsearch-full-$XS_VERSION.tar.bz2 \
    && cd xunsearch-full-$XS_VERSION \
    && sh setup.sh --prefix=$XS_PREFIX

RUN echo '' >> $XS_PREFIX/bin/xs-ctl.sh
RUN echo 'tail -f /dev/null' >> $XS_PREFIX/bin/xs-ctl.sh

VOLUME $XS_DATA
EXPOSE 8383
EXPOSE 8384

WORKDIR $XS_PREFIX
RUN echo "#!/bin/sh" > bin/xs-docker.sh
RUN echo "echo -n > tmp/docker.log" >> bin/xs-docker.sh
RUN echo "bin/xs-indexd -l tmp/docker.log -k start" >> bin/xs-docker.sh
RUN echo "sleep 1" >> bin/xs-docker.sh
RUN echo "bin/xs-searchd -l tmp/docker.log -k start" >> bin/xs-docker.sh
RUN echo "sleep 1" >> bin/xs-docker.sh
RUN echo "tail -f tmp/docker.log" >> bin/xs-docker.sh

ENTRYPOINT ["sh"]
CMD ["bin/xs-docker.sh"]
