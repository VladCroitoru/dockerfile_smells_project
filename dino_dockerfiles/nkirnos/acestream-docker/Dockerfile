FROM ubuntu:14.04
MAINTAINER nkirnos <nkirnos@gmail.com>

COPY sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y wget build-essential checkinstall gcc-multilib g++-multilib libffi-dev libffi6 libffi6-dbg python-crypto python-mox3 python-pil python-ply libssl-dev \
    zlib1g-dev libexpat1-dev libbluetooth-dev libgdbm-dev dpkg-dev quilt autotools-dev libtinfo-dev libncursesw5-dev tk-dev blt-dev zlib1g-dev \
    libbz2-dev  libsqlite3-dev libgpm2 mime-support netbase net-tools bzip2 libncursesw5-dev libsqlite3-dev tk-dev \
    libgdbm-dev libc6-dev
RUN  wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz && tar xvf Python-2.7.13.tgz && cd Python-2.7.13 && ./configure --enable-ipv6 \
&& make && make install

RUN echo "deb http://repo.acestream.org/ubuntu/ trusty main" >> /etc/apt/sources.list
RUN wget -O - http://repo.acestream.org/keys/acestream.public.key | sudo apt-key add -
RUN apt-get update && apt-get install -y acestream-engine python-pip supervisor
COPY AcePHProxy /usr/local/src/AcePHProxy
RUN apt-get install -y php5-cli php5-dev php-pear && pecl install ncurses && echo "extension=ncurses.so" > /etc/php5/mods-available/ncurses.ini && ln -s /etc/php5/mods-available/ncurses.ini /etc/php5/cli/conf.d/ncurses.ini 
RUN apt-get install -y screen
RUN rm -rf /var/lib/apt/lists/*

COPY supervisor.conf /etc/supervisor/supervisor.conf
EXPOSE 62062 8001
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh