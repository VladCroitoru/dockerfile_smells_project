FROM ubuntu:16.04
MAINTAINER Thiago Martins <rogue.thiago@gmail.com>
 
ENV DISPLAY=:0
ENV RESOLUTION=1366x768
 
WORKDIR /root

RUN apt-get -y update && \
    apt-get -y install xvfb git wget xz-utils

RUN wget https://nodejs.org/dist/v6.9.1/node-v6.9.1-linux-x64.tar.xz && \
    tar -C /usr/local --strip-components 1 -xJf node*tar.xz && \
    rm node*tar.xz

RUN npm install -g bower && \
    echo '{ "allow_root": true, "gitUseHttps": true }' > ~/.bowerrc && \
    echo "N\n" | bower

#but in need... we can launch chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    CHROME_FILE=`whereis -b google-chrome | awk '{print $2}'` && \
    cp $CHROME_FILE "$CHROME_FILE".old && \
    cat "$CHROME_FILE".old | sed 's/exec -a "$0" "$HERE\/chrome"  "$@"/exec -a "$0" "$HERE\/chrome" "$@" --no-default-browser-check --no-first-run --no-sandbox --user-data-dir/' > $CHROME_FILE && \
    rm "$CHROME_FILE".old

#Prevent git clone errors
#See -> https://github.com/npm/npm/issues/5257
RUN git config --global url."https://github.com/".insteadOf git@github.com: && \
    git config --global url."https://".insteadOf git://

ADD startup.sh /

RUN chmod +x /startup.sh
    
ENTRYPOINT ["/startup.sh"]
