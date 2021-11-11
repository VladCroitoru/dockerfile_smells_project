FROM debian:jessie
RUN apt-get update --fix-missing
RUN apt-get upgrade
RUN apt-get install -y python build-essential cmake git-core graphicsmagick imagemagick wget libfreetype6 \
  libfontconfig bzip2 curl libtheora0 poppler-utils unzip zip libav-tools libavcodec-extra \
  checkinstall libmad0-dev libsndfile1-dev libgd2-xpm-dev libboost-filesystem-dev libboost-program-options-dev libboost-regex-dev libid3tag0-dev libid3tag0
  #libmad0-dev libsndfile1-dev
#RUN apt-get install -y vim htop screen ncdu cmake

RUN mkdir deps && cd deps

WORKDIR deps

RUN git clone https://github.com/bbcrd/audiowaveform.git
RUN cd audiowaveform && wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz && \
  tar xzf release-1.8.0.tar.gz && \
  ln -s googletest-release-1.8.0/googletest googletest && \
  ln -s googletest-release-1.8.0/googlemock googlemock

RUN cd audiowaveform && mkdir build && cd build && cmake .. && make && make install

ENV PHANTOMJS_VERSION=2.1.1
RUN wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
RUN tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp
RUN mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /usr/local/phantomjs
RUN ln -s /usr/local/phantomjs/bin/phantomjs /usr/bin/phantomjs
RUN ln -s /usr/bin/avconv /usr/bin/ffmpeg
RUN ln -s /usr/bin/avprobe /usr/bin/ffprobe

RUN for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 7.8.0

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /deps