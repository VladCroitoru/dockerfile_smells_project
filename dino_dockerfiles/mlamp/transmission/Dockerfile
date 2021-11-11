FROM ubuntu:latest
MAINTAINER Margus Lamp <margus.lamp+github@gmail.com>

# Copy neccessary scripts
COPY unrarall /usr/local/bin/
RUN chmod a+x /usr/local/bin/unrarall

COPY torrentdone.sh /usr/local/bin/
RUN chmod a+x /usr/local/bin/torrentdone.sh


# Install transmission, curl, unrar and cksfv
RUN export DEBIAN_FRONTEND='noninteractive' && \
    apt-get update -qq && \
    apt-get install -qqy software-properties-common python-software-properties && \
    add-apt-repository multiverse && \
    add-apt-repository ppa:transmissionbt/ppa && \
    apt-get update -qq && \
    apt-get install -qqy --no-install-recommends transmission-daemon curl unrar ca-certificates cksfv \
                $(apt-get -s dist-upgrade|awk '/^Inst.*ecurity/ {print $2}')

# Copy local transmission settings
COPY settings.json /var/lib/transmission-daemon/.config/transmission-daemon/
RUN dir="/var/lib/transmission-daemon" && \
    rm -rf $dir/info && \
    mv $dir/.config/transmission-daemon $dir/info && \
    rmdir $dir/.config && \
    usermod -d $dir debian-transmission && \
    [ -d $dir/downloads ] || mkdir -p $dir/downloads && \
    [ -d $dir/incomplete ] || mkdir -p $dir/incomplete && \
    [ -d $dir/info/blocklists ] || mkdir -p $dir/info/blocklists && \
    file="$dir/info/settings.json" && \
    chown -Rh debian-transmission. $dir

# Cleanup apt stuff
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*

# Expose transmission directory
VOLUME ["/var/lib/transmission-daemon"]

# Copy entry script
COPY transmission.sh /usr/bin/

# Expose ports for transmission
EXPOSE 9091 51413/tcp 51413/udp

#Run entry script
ENTRYPOINT ["transmission.sh"]
