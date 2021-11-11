FROM onsdigital/java-component

# Phantom.js
WORKDIR /usr/phantom
RUN apt-get install -y tar bzip2
ADD https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2 /usr/phantom/phantom.tar.bz2
RUN tar -xvjf phantom.tar.bz2
RUN mv phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/local/bin/
