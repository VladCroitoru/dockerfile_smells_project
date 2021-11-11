FROM phusion/baseimage:0.9.22

RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 9E3E53F19C7DE460 \
 && add-apt-repository 'deb http://repo.aptly.info/ squeeze main' \
 && apt-get update -q && apt-get install -y -q \
    aptly \
    realpath \
 && rm -rf /var/lib/apt/lists/*

ADD bin/ /usr/local/bin/

ENTRYPOINT ["/sbin/my_init", "--", "/usr/local/bin/startup.sh"]
