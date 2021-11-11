FROM ruby:2.1
RUN curl -o phantomjs.tar.gz -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar -xvf phantomjs.tar.gz

RUN mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin
RUN echo "export phantomjs=/usr/bin/phantomjs" > .bashrc
RUN apt-get install -y libfreetype6 libfontconfig1
RUN gem install wraith --no-rdoc --no-ri
RUN gem install aws-sdk --no-rdoc --no-ri
# Make sure decent fonts are installed. Thanks to http://www.dailylinuxnews.com/blog/2014/09/things-to-do-after-installing-debian-jessie/
RUN echo "deb http://ftp.us.debian.org/debian jessie main contrib non-free" | tee -a /etc/apt/sources.list
RUN echo "deb http://security.debian.org/ jessie/updates contrib non-free" | tee -a /etc/apt/sources.list
COPY phantomjs_hawk.sh /phantomjs_hawk.sh
RUN chmod 755 /phantomjs_hawk.sh && \
    apt-get update && \
    apt-get install -y ttf-freefont ttf-mscorefonts-installer ttf-bitstream-vera ttf-dejavu ttf-liberation

WORKDIR /app
ENTRYPOINT [ "wraith", "capture" ]
CMD [ "configs/capture.yaml" ]
