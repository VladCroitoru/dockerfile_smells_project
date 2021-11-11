FROM debian:jessie

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r -g 1000 crawl && useradd -r -m -g crawl -u 1000 crawl

# install required packages
RUN apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
    ca-certificates locales wget git python3-pip

# set UTF-8 locale 
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN touch /etc/locale.conf \
	&& echo -e "LANG=en_US.UTF-8 \nLANGUAGE=en_US.UTF-8 \nLC_CTYPE=en_US.UTF-8 \nLC_ALL=en_US.UTF-8 \n" > /etc/locale.conf \
	&& locale-gen en_US.UTF-8 \
	&& echo "146\n3\n" | dpkg-reconfigure locales

# clone from github latest crawl version
RUN git clone https://github.com/crawl/crawl.git && cd /crawl \
	&& git checkout 0.18.1 \
        && git submodule update --init \
	&& mkdir -p /crawl/crawl-ref/source/rcs \
	&& mkdir -p /crawl/crawl-ref/source/saves

# install required packages for crawl build
RUN apt-get update \ 
	&& apt-get install --no-install-recommends --no-install-suggests -y \
    build-essential \
    libncursesw5-dev \
    bison \
    flex \
    liblua5.1-0-dev \
    libsqlite3-dev \
    libz-dev \
    pkg-config \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-dev \
    libfreetype6-dev \
    libpng-dev \
    ttf-dejavu-core \
        && rm -rf /var/lib/apt/lists/*

# install pip and tornado for web server
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install tornado==3.2.2

# make webtile version
RUN cd /crawl/crawl-ref/source && make WEBTILES=y

COPY data/docker-entrypoint.sh /entrypoint.sh
RUN chown -R crawl:crawl /entrypoint.sh \
	&& chmod 777 /entrypoint.sh \
	&& chown -R crawl:crawl /crawl
 

WORKDIR /crawl/crawl-ref/source
VOLUME /crawl
VOLUME /crawl/crawl-ref/source/saves
EXPOSE 8080
ENTRYPOINT ["/entrypoint.sh"]

#USER crawl
CMD ["python", "./webserver/server.py"]
