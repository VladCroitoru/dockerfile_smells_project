FROM ubuntu

MAINTAINER http://obcon.de Marco Obermeyer <marco.obermeyer@obcon.de>

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y wget unzip

RUN wget https://www.browserstack.com/browserstack-local/BrowserStackLocal-linux-x64.zip && \ 
    unzip BrowserStackLocal-linux-x64.zip && \
    rm BrowserStackLocal-linux-x64.zip && \
    chmod +x BrowserStackLocal && \
    mv BrowserStackLocal /usr/local/bin


ENTRYPOINT ["/usr/local/bin/BrowserStackLocal"]
