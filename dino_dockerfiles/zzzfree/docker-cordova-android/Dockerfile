FROM beevelop/cordova

CP sources.list /etc/apt/

RUN apt-get update

RUN cd /tmp \
    && cordova create test \
    && cd /tmp/test \
    && cordova platform add android \
    && cordova build android
