FROM valtri/docker-puppet-debian:8
MAINTAINER František Dvořák <valtri@civ.zcu.cz>

# ==== system ====

COPY ./krb5.conf /etc

# ==== puppet ====

RUN apt-get update \
&& apt-get install -y ca-certificates \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
RUN puppet module install cesnet-site_hadoop

# ==== hadoop ====

# not needed, just perform some less fragile steps sooner
COPY ./java.pp /root
RUN apt-get update \
&& puppet apply /root/java.pp --test; test $? -eq 2 \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# the main deployment
COPY ./site.pp /root
RUN puppet apply /root/site.pp --test; test $? -eq 2 \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# XXX: belongs to cesnet-spark puppet module
COPY ./hadoop-spark2.sh /etc/profile.d/
COPY ./hadoop-spark2.csh /etc/profile.d/

# niceties
RUN apt-get update \
&& apt-get install -y bzip2 less mc screen ssh pbzip2 pigz vim \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/share/mc/bin/mc.sh /etc/profile.d/
RUN ln -s /usr/share/mc/bin/mc.csh /etc/profile.d/
