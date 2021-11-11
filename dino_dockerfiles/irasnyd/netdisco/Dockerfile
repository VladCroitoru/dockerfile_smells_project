FROM centos:7
MAINTAINER Ira W. Snyder <isnyder@lcogt.net>

# netdisco-web runs on port 5000
EXPOSE 5000
ENTRYPOINT [ "/init" ]

ENV NETDISCO_HOME "/netdisco"
ENV NETDISCO_VERSION 2.036012_003
ENV NETDISCO_MIBS_VERSION 4.003

# install and update packages
RUN yum -y install epel-release \
        && yum -y install \
                automake \
                bzip2 \
                gcc \
                gzip \
                make \
                net-snmp-devel \
                net-snmp-perl \
                openssl-devel \
                openssl-perl \
                perl-core \
                perl-DBD-Pg \
                postgresql \
                supervisor \
                tar \
        && yum -y update \
        && yum -y clean all

# Install netdisco
# https://metacpan.org/pod/App::Netdisco
RUN mkdir -p "$NETDISCO_HOME" \
        && cd "$NETDISCO_HOME" \
        && curl -L http://cpanmin.us/ | perl - --notest --local-lib $NETDISCO_HOME/perl5 App::Netdisco@$NETDISCO_VERSION \
        && rm -rf /root/.cpanm

# Add netdisco to the PATH
ENV PATH $NETDISCO_HOME/perl5/bin:$PATH

# Fetch OUI file and MIBS manually. This makes sure that we don't need Internet
# access to start the container, since we already have these files built in.
RUN cd "$NETDISCO_HOME" \
        && curl -L --connect-timeout 60 --retry 10 https://raw.githubusercontent.com/netdisco/upstream-sources/master/ieee/oui.txt > oui.txt \
        && curl -L --connect-timeout 60 --retry 10 https://github.com/netdisco/netdisco-mibs/archive/$NETDISCO_MIBS_VERSION.tar.gz > netdisco-mibs-$NETDISCO_MIBS_VERSION.tar.gz \
        && tar xzf netdisco-mibs-$NETDISCO_MIBS_VERSION.tar.gz \
        && mv netdisco-mibs-$NETDISCO_MIBS_VERSION netdisco-mibs \
        && rm -f netdisco-mibs-$NETDISCO_MIBS_VERSION.tar.gz

# Install operating system configuration
COPY docker/ /
