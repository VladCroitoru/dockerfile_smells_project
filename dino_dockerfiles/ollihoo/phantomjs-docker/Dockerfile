FROM debian:jessie
RUN echo "deb http://ftp.debian.org/debian jessie non-free contrib" > /etc/apt/sources.list.d/jessie.list
RUN apt-get update
RUN apt-get install -y bzip2 wget libfreetype6 libfontconfig
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar -xjf phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN rm *.bz2
RUN mv phantomjs-* /usr/share/phantomjs
RUN ln -s /usr/share/phantomjs/bin/phantomjs /usr/bin/phantomjs
COPY phantomjs.sh /phantomjs.sh
RUN chmod +x /phantomjs.sh
CMD [ "/phantomjs.sh" ]
