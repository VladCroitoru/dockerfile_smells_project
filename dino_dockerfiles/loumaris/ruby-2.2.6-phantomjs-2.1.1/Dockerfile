FROM ruby:2.2.6
MAINTAINER christian.heimke@loumaris.com

ENV PHANTOM_JS "phantomjs-2.1.1-linux-x86_64"

RUN apt-get update -qq && apt-get install -y -qq build-essential \
                                                postgresql postgresql-contrib libpq-dev \
                                                cmake qt5-default libqt5webkit5-dev \
                                                gstreamer1.0-plugins-base gstreamer1.0-tools \
                                                gstreamer1.0-x openssh-client \
                                                chrpath libssl-dev libxft-dev \
                                                libfreetype6 libfreetype6-dev \
                                                libfontconfig1 libfontconfig1-dev

WORKDIR /tmp

RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 && \
    tar xvjf $PHANTOM_JS.tar.bz2 && \
    rm -rf $PHANTOM_JS.tar.bz2 && \
    mv $PHANTOM_JS /usr/local/share && \
    ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

CMD [ 'irb' ]
