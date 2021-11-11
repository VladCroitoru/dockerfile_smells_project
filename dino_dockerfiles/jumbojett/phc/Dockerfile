FROM ubuntu:trusty

# Set correct environment variables.
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get install -y vim git clang-3.5 llvm libgc-dev libxerces-c2-dev wget patch build-essential software-properties-common curl libboost1.55-all-dev python-software-properties libtool autoconf
# Install Boost
WORKDIR /tmp

RUN wget ftp://ftp.gnu.org/gnu/automake/automake-1.15.tar.gz && \
    tar -xzf automake-1.15.tar.gz && \
    cd automake-1.15 && ./configure && \
    make && make install


RUN apt-get -y install libxml2-dev

RUN mkdir -p /root/phc
WORKDIR /root/phc
COPY . /root/phc
#RUN git clone https://github.com/TheSin-/phc.git /root/phc
RUN cd /root/phc

RUN wget http://museum.php.net/php5/php-5.2.17.tar.gz
RUN tar zxvf php-5.2.17.tar.gz
RUN cd php-5.2.17 && CFLAGS="-O0 -ggdb3" ./configure --enable-debug --enable-maintainer-zts --enable-embed
RUN cd php-5.2.17 && wget http://storage.googleapis.com/google-code-attachments/php52-backports/issue-16/comment-2/libxml29_compat.patch && patch -p0 < libxml29_compat.patch
RUN cd php-5.2.17 && make -j 4 && make install


RUN chmod +x autogen.sh && ./autogen.sh
RUN ./configure --with-xerces --disable-static
#RUN CPPFLAGS="-I/usr/local/include/php/sapi/embed/" CXXFLAGS="-I/usr/local/include/php/sapi/embed/" CFLAGS="-I/usr/local/include/php/sapi/embed/" ./configure
RUN make -j 4
RUN make install