FROM ubuntu:trusty
# Update packages
RUN echo "deb http://archive.ubuntu.com/ubuntu/ precise universe" >> /etc/apt/sources.list && apt-get update
# install curl, wget,sql ,server
RUN apt-get install -y libpcre3 libpcre3-dev libssl-dev make gcc g++ build-essential cmake curl wget git unzip python-software-properties python-setuptools software-properties-common debian-archive-keyring python-pip openssl openssh-server
RUN add-apt-repository -y ppa:ondrej/php && apt-get update
RUN apt-get install -y --force-yes mariadb-server mariadb-client memcached php7.0 php7.0-fpm php7.0-mysql php7.0-curl php7.0-gd php7.0-imap php7.0-json php7.0-cli php7.0-xml php-memcache
# Install tengine
ADD https://github.com/alibaba/tengine/archive/master.tar.gz .
RUN tar zxvf /master.tar.gz && cd tengine-master && ./configure --with-http_concat_module && make && make install && rm -rf /master.tar.gz /tengine-master
# Install Supervisor & tingyun & shadowsocks
RUN /usr/bin/easy_install supervisor && /usr/bin/easy_install supervisor-stdout
RUN wget http://download.networkbench.com/agent/php/2.7.0/tingyun-agent-php-2.7.0.x86_64.deb?a=1498149881851 -O tingyun-agent-php.deb
RUN wget http://download.networkbench.com/agent/system/1.1.1/tingyun-agent-system-1.1.1.x86_64.deb?a=1498149959157 -O tingyun-agent-system.deb
RUN sudo dpkg -i tingyun-agent-php.deb && sudo dpkg -i tingyun-agent-system.deb && rm -rf /tingyun-*.deb
RUN pip install shadowsocks
# Start
VOLUME ["/data"]
EXPOSE 22 80 3306 8388 9001 11211
CMD ["sh","-c"," \
    cd /data/www/ && git init && git remote add origin $(echo $git_url) && git pull origin master; \
    cp -f /data/www/configs/run.sh /run.sh && sed -i -e 's/\r//g' /run.sh && sed -i -e 's/^M//g' /run.sh && chmod +x /*.sh ; \
    . /run.sh \
"]
