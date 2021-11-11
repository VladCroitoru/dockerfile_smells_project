FROM codeception/codeception

RUN apt-get -y update && \    
    apt-get -y install libfontconfig libpq5 postgresql-client && \
    apt-get -y autoremove && \
    apt-get -y clean && \

    curl -L https://github.com/medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
        -o /tmp/phantomjs.tar.bz2 && \
    tar xjf /tmp/phantomjs.tar.bz2 -C /tmp && \
    cp /tmp/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin && \
    rm -rf /tmp/*
