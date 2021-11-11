FROM ubuntu:15.04

ADD . /munin
RUN apt-get update -qq && apt-get upgrade -y && RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive \
    apt-get install -y -qq make pkg-config libglib2.0-dev libxml2-dev libcairo2-dev libpango1.0-dev python-sphinx rrdtool sqlite3 \
 && sed -i'' -e 's/install/install -y -qq/' /munin/dev_scripts/deps \
 && /munin/dev_scripts/deps \
 && /munin/dev_scripts/install 1 \
 && (yes | /munin/Build installdeps) \
 && make -C /munin clean && make -C /munin && make -C /munin install \
 && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN find /usr/local/bin -type f -perm -a-rx -print0 \
	| xargs -0 -n 1 -t perl -pi -e "s,bin/perl -T,bin/perl,"
RUN sed -i'' -e 's/USER_ID == 0/USER_ID == 42/' /usr/local/share/perl/*/Munin/Master/Utils.pm \
 && echo 'includedir /etc/munin/munin-conf.d' > /usr/local/etc/munin/munin.conf

VOLUME ["/etc/munin/munin-conf.d", "/var/lib/munin"]
EXPOSE 4948
