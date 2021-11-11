# Copyright 2018 SpiderOak, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:16.04
MAINTAINER David Hain <dhain@spideroak-inc.com>

ENV NAGIOS_BRANCH nagios-4.3.4
ENV NAGIOS_PLUGINS_BRANCH release-2.2.1
ENV NRPE_BRANCH nrpe-3.2.1
ENV NAGIOS_NSCA nsca-2.7.2.tar.gz

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl \
    apt-transport-https && \
    curl -sL https://packages.pagerduty.com/GPG-KEY-pagerduty | apt-key add - && \
    echo 'deb https://packages.pagerduty.com/pdagent deb/' > /etc/apt/sources.list.d/pdagent.list && \
    apt-get update && \
    mv /bin/systemctl /bin/systemctl.bak && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    pdagent \
    pdagent-integrations && \
    mv /bin/systemctl.bak /bin/systemctl && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    php7.0-fpm \
    fcgiwrap \
    nginx \
    runit \
    iputils-ping \
    mtr \
    netcat \
    build-essential \
    automake \
    autoconf \
    mailutils \
    m4 \
    gettext \
    git \
    php-gd \
    libgd-dev \
    libssl-dev \
    libwww-perl \
    libjson-perl \
    libcgi-pm-perl \
    libdbd-pg-perl \
    libswitch-perl \
    unzip && \
    useradd nagios && \
    usermod -aG nagios www-data && \
    rm /etc/nginx/sites-*/default && \
    setcap cap_net_raw+ep /usr/bin/mtr && \
    cd /tmp && \
    git clone https://github.com/NagiosEnterprises/nagioscore.git -b $NAGIOS_BRANCH && \
    cd nagioscore && \
    ./configure \
    --prefix=/opt/nagios \
    --exec-prefix=/opt/nagios \
    --with-command-user=nagios \
    --with-command-group=nagios \
    --with-nagios-user=nagios \
    --with-nagios-group=nagios \
    --enable-event-broker && \
    make all && \
    make install && \
    make install-init && \
    make install-config && \
    make install-commandmode && \
    cp -R contrib/eventhandlers/ /opt/nagios/libexec/ && \
    chown -R nagios:nagios /opt/nagios/libexec/eventhandlers && \
    cd $WORKDIR && \
    rm -rf /tmp/nagioscore && \
    cd /tmp && \
    git clone https://github.com/nagios-plugins/nagios-plugins.git -b $NAGIOS_PLUGINS_BRANCH && \
    cd nagios-plugins && \
    ./tools/setup && \
    ./configure --prefix=/opt/nagios && \
    make && \
    make install && \
    mkdir -p /usr/lib/nagios/plugins && \
    ln -sf /opt/nagios/libexec/utils.pm /usr/lib/nagios/plugins && \
    cd $WORKDIR && \
    rm -rf /tmp/nagios-plugins && \
    cd /tmp && \
    git clone https://github.com/NagiosEnterprises/nrpe.git -b $NRPE_BRANCH && \
    cd nrpe && \
    ./configure \
    --with-ssl=/usr/bin/openssl \
    --with-ssl-lib=/usr/lib/x86_64-linux-gnu && \
    make check_nrpe && \
    cp src/check_nrpe /opt/nagios/libexec/ && \
    cd $WORKDIR && \
    rm -rf /tmp/nrpe && \
    curl -sLo /opt/nagios/etc/objects/pagerduty.cfg https://raw.githubusercontent.com/PagerDuty/pdagent-integrations/master/pagerduty_nagios.cfg && \
    chown nagios:nagios /opt/nagios/etc/objects/pagerduty.cfg && \
    chmod 664 /opt/nagios/etc/objects/pagerduty.cfg && \
    curl -sL https://raw.githubusercontent.com/mdcollins05/pd-nag-connector/master/pagerduty.cgi | \
    sed "s|^\(\s\+'command_file' => \)'[^']\+'|\1'"`awk -F= '/command_file/ { print $2 }' /opt/nagios/etc/nagios.cfg`"'|" > /opt/nagios/sbin/pagerduty.cgi && \
    chown nagios:nagios /opt/nagios/sbin/pagerduty.cgi && \
    chmod 775 /opt/nagios/sbin/pagerduty.cgi && \
    apt-get purge --autoremove -y \
    build-essential \
    git && \
    rm -rf /var/lib/apt/lists/*

# Install NSCA
RUN mkdir -p /opt/nagios/nagios4-nsca && \
    cd /opt/nagios/nagios4-nsca && \
    curl -v -L http://prdownloads.sourceforge.net/sourceforge/nagios/$NAGIOS_NSCA | tar -zxp --strip-components 1 && \
    ./configure \
    --with-nsca-user=nagios \
    --with-nsca-grp=nagios && \
    make all && \
    cd /opt/nagios/nagios4-nsca && \
    cp sample-config/nsca.cfg sample-config/send_nsca.cfg /opt/nagios/etc/ && \
    cp src/send_nsca src/nsca /opt/nagios/bin/

ADD files /

EXPOSE 80

VOLUME "/opt/nagios/var" "/opt/nagios/etc" "/opt/nagios/libexec"

WORKDIR /opt/nagios

ENTRYPOINT ["/entrypoint.sh"]
