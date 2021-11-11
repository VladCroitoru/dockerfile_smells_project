FROM phusion/baseimage

RUN apt-get update \
 && apt-get install -y telnet inetutils-ping curl unzip vim locales \
 && dpkg-reconfigure -f noninteractive locales \
 && /usr/sbin/update-locale LANG=en_US.UTF-8 \
 && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
 && locale-gen

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
