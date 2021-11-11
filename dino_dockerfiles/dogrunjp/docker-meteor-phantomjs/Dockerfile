FROM ubuntu
RUN apt-get update
RUN apt-get install -y \
    curl \
    wget

RUN apt-get install -y build-essential chrpath libssl-dev libxft-dev
RUN apt-get install -y libfreetype6 libfreetype6-dev
RUN apt-get install -y libfontconfig1 libfontconfig1-dev
RUN apt-get install -y npm

WORKDIR ~/
RUN export PHANTOM_JS="phantomjs-1.9.8-linux-x86_64" && \
    wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 && \
    mv $PHANTOM_JS.tar.bz2 /usr/local/bin && \
    cd /usr/local/bin && \
    tar xvjf $PHANTOM_JS.tar.bz2 && \
    ln -sf /usr/local/bin/$PHANTOM_JS/bin/phantomjs  /usr/local/bin/phantomjs

RUN curl install.meteor.com | /bin/sh

RUN meteor create hello && \
    cd hello && \
    meteor add d3 && \
    meteor remove autopublish
    meteor add meteorhacks:npm

CMD ["meteor"]    
