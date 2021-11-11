FROM ubuntu:16.04

LABEL maintainer="Jaeyoung Chun (jaeyoung.chun@weizmann.ac.il)"

ENV BEAGLE_LIB_VERSION="2_1_2"
ENV BEAST_VERSION="2.4.7"
ENV BEASTvntr_VERSION="0.1.1"

RUN apt-get update -y \
    && apt-get install -y wget openjdk-8-jre gcc make autoconf automake libtool pkg-config unzip

WORKDIR /tmp

# install beagle-lib
RUN wget https://github.com/beagle-dev/beagle-lib/archive/beagle_release_${BEAGLE_LIB_VERSION}.tar.gz \
    && tar xvzf beagle_release_${BEAGLE_LIB_VERSION}.tar.gz \
    && cd beagle-lib-beagle_release_${BEAGLE_LIB_VERSION} \
    && ./autogen.sh \
    && ./configure --prefix=/usr/local CPPFLAGS="-mno-avx -mno-avx2" \
    && make install

# set LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH=/lib:/usr/lib:/usr/local/lib
RUN ldconfig

# install beast2
RUN wget https://github.com/CompEvol/beast2/releases/download/v${BEAST_VERSION}/BEAST.v${BEAST_VERSION}.Linux.tgz \
    && tar xvzf BEAST.v${BEAST_VERSION}.Linux.tgz \
    && mv beast /usr/local/bin/beast2 \
    && cp /usr/local/bin/beast2/bin/* /usr/local/bin \
    && cp /usr/local/bin/beast2/lib/* /usr/local/lib

# install BEASTvntr
RUN wget https://github.com/arjun-1/BEASTvntr/releases/download/v${BEASTvntr_VERSION}/BEASTvntr.addon.v${BEASTvntr_VERSION}.zip \
    && mkdir -p ~/.beast/2.4/BEASTvntr \
    && unzip BEASTvntr.addon.v${BEASTvntr_VERSION}.zip -d ~/.beast/2.4/BEASTvntr

# clean up
RUN rm -rf /tmp/BEAST.v${BEAST_VERSION}.Linux.tgz /tmp/BEASTvntr.addon.v${BEASTvntr_VERSION}.zip \
    && rm -rf /tmp/beagle-lib-beagle_release_${BEAGLE_LIB_VERSION} /tmp/beagle_release_${BEAGLE_LIB_VERSION}.tar.gz

WORKDIR /root/.beast/2.4
ENTRYPOINT ["/usr/local/bin/beauti", "-template", "/usr/local/bin/beast2/templates/Standard.xml"]
