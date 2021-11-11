FROM ubuntu:14.04.3
RUN : \
 && apt-get update \
 && apt-get install -y git unzip make coreutils gcc binutils build-essential libexpat1-dev libgmp-dev libncurses5-dev libssl-dev libpcap-dev byacc flex libreadline-dev python-dev python-pastedeploy python-paste python-twisted python-setuptools python-pip libxml2-dev libxslt-dev ethtool \
 && mkdir -p /usr/local/etc/lagopus \
 && git clone https://github.com/hibitomo/handson_files.git \
 && cp handson_files/lagopus.dsl /usr/local/etc/lagopus/ \
 && git clone https://github.com/lagopus/lagopus \
 && cd lagopus \
 && ./configure \
 && make -j \
 && make install \
 && apt-get clean all \
 && :
ADD init.sh /
CMD /init.sh

