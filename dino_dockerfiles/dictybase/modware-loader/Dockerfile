FROM perl:5.24
MAINTAINER Siddhartha Basu <siddhartha-basu@northwestern.edu>

ADD https://northwestern.box.com/shared/static/3n0wdp04075oyrnytznn9mzc3k9o92c1.rpm /rpms/
ADD https://northwestern.box.com/shared/static/o2gd3o70sik5liw43hiomusmu0262auw.rpm /rpms/
ADD https://northwestern.box.com/shared/static/nsflzsbm2xmcf46z1ybiustosqkdskbb.rpm /rpms/

RUN apt-get update && \
    apt-get -y install alien libaio1 libdb-dev libexpat1-dev && \
    mkdir -p /rpms && \
    alien -i /rpms/*.rpm && \
    echo '/usr/lib/oracle/11.2/client64/lib' > /etc/ld.so.conf.d/oracle.conf && \
    echo 'export ORACLE_HOME=/usr/lib/oracle/11.2/client64' > /etc/profile.d/oracle.sh \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /var/lib/dpkg/lock

ENV ORACLE_HOME /usr/lib/oracle/11.2/client64/
ENV LD_LIBRARY_PATH /usr/lib/oracle/11.2/client64/lib/

ARG curruid
ARG user
ADD . /tmp/
RUN cd /tmp \
    && cpanm -n --quiet --installdeps . \
    && cpanm -n --quiet DBD::Oracle DBD::Pg Math::Base36 String::CamelCase LWP::Protocol::https Child Dist::Zilla \
    && dzil authordeps --missing | cpanm -n --quiet  \
    && perl Build.PL \
    && ./Build install \
    && rm -fr /rpms \
    && rm -rf /tmp/*
# Add an user that will be used for install purpose
RUN useradd -m -s /bin/bash -c "Docker image user" -u $curruid $user 
USER $user
WORKDIR /usr/src/modware

ENV HARNESS_OPTIONS j6

CMD perl Build.PL && ./Build test
