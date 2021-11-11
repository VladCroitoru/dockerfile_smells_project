FROM ubuntu:16.04
MAINTAINER MEENACHISUNDARAM V <ms.v@initcron.org>

RUN apt-get update -y && \
    apt-get install software-properties-common wget unzip curl ruby-full build-essential zlib1g-dev libz-dev libiconv-hook1 libiconv-hook-dev libcurl4-openssl-dev python-software-properties default-jre default-jdk  -y

RUN apt-get install texlive-full -y

RUN add-apt-repository ppa:inkscape.dev/stable -y

RUN apt-get update -y

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get install nodejs inkscape -y

RUN cd /tmp && wget https://github.com/IDPF/epubcheck/releases/download/v4.0.1/epubcheck-4.0.1.zip && \
    wget http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz && \
    wget -nv -O- https://download.calibre-ebook.com/linux-installer.py | python -c "import sys; main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main()" && \
    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2

RUN cd /tmp && tar -xvzf kindlegen_linux_2.6_i386_v2_9.tar.gz && mv kindlegen /usr/bin/ && \
    unzip epubcheck-4.0.1.zip && mv epubcheck-4.0.1 /usr/bin/ && \
    tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2  && mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/

RUN rm -rf /tmp/*

RUN mkdir -p /softcover

RUN gem install softcover

EXPOSE 4000

WORKDIR /softcover
