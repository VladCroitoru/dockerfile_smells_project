FROM ubuntu:15.04
MAINTAINER Aevum Decessus <aevum@decess.us>

ADD https://download-cdn.getsync.com/2.1.0/linux-x64/BitTorrent-Sync_x64.tar.gz /tmp/sync.tgz
RUN tar -xf /tmp/sync.tgz -C /usr/sbin btsync && rm -f /tmp/sync.tgz

# Pull Script from https://gist.github.com/sciurius/787e99af74132b62b397
ADD https://gist.githubusercontent.com/sciurius/787e99af74132b62b397/raw/b3f5cccda9bb7f3acf1248ae097a5bc3a888e837/btsync-keygen /usr/sbin/btsync-keygen
RUN chmod 755 /usr/sbin/btsync-keygen
CMD ["/usr/sbin/btsync-keygen"]
