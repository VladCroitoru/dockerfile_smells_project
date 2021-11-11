FROM jpazdyga/centos7-base
MAINTAINER Jakub Pazdyga <jakub.pazdyga@ft.com>

ENV SCUMBLR_EMAIL testuser@somedomain.com
ENV SCUMBLR_PASSWD scumblrtest

RUN rpmdb --rebuilddb && \ 
    rpmdb --initdb && \
    yum clean all && \
    yum --noplugins -y update && \
    yum --noplugins -y install wget \ 
		   curl \
		   bind-utils \
		   screen \
	   	   libxslt \
		   libxslt-devel \
		   libxml2-devel \
		   libxml2 \
		   libxml2-devel \
		   bison-devel\ 
		   bison \
		   libffi \
		   libffi-devel \
		   autoconf \
		   readline \
		   readline-devel \
		   libtool \
		   sqlite-devel \
		   ImageMagick-devel \
		   ImageMagick \
		   ruby-devel \
		   ruby-libs \
		   rubygem-bundler \
		   zlib-devel \ 
		   zlib-static \ 
		   zlib \
		   python \
		   libffi-devel \
		   openssl-devel \
		   libpqxx-devel \
		   gcc \
		   gcc-c++ \
		   libpqxx-devel \
		   openssh \
                   openssl \
		   openssl-devel \
                   openssl-libs \
                   psmisc \
                   openssh-server \
                   git \
		   unzip \
		   python-setuptools \
                   python-pip \
		   redis \
		   hiredis-devel \
		   hiredis \
		   python-redis

RUN pip install --upgrade pip && \
      pip install --upgrade setuptools

RUN useradd -d /home/monkey -G wheel -m -s /bin/bash monkey && \
	su monkey -c "ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa" && \
	ssh-keygen -A && \
	echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAxLPLjUQf35uzbNGiCiVkOpeXOaO4JdC0GGkRTRhgSeKdu4Nz2iADET5bYBps27OCnk7JmWp3PiNbs6inMazHMylxB8BeV1Q9p+yMZLpuGdziokt4Z8sVDjgMkJPS0Ob74GE2aIfqx/gxTgf2WGQTNlCWP53nb3ccjQXW2b8jK39VCLw5VPE3YMojfGdM9BMhMOUdut3xnIJNnjivuZw9SZM746/PCvxvB/h+nE6u/3QP7D2xhEAXusxnctvOz2LWBf5rXrndAf4ENqOe6JK7LWGVTax2NgXc0pVJ53/+Ghhi2zYBuEaQGiOc7qeblJEUqrMXPij50LcE0ya10cmdAw==" > /home/monkey/.ssh/authorized_keys && \
	echo "Defaults:postgres !requiretty" >> /etc/sudoers

RUN sed -i \
	-e 's/^PasswordAuthentication yes/PasswordAuthentication no/g' \
	-e 's/^#PermitRootLogin yes/PermitRootLogin yes/g' \
	-e 's/^#UseDNS yes/UseDNS no/g' \
	/etc/ssh/sshd_config

RUN sed -i \
        -e 's/^%wheel\tALL=(ALL)\tALL/#%wheel\tALL=(ALL)\tALL/g' \
        /etc/sudoers && \
        echo -e "%wheel\tALL=(ALL)\tNOPASSWD:\tALL" >> /etc/sudoers

ADD ruby_config.sh /usr/sbin/ruby_config.sh
RUN mkdir -p /usr/local/share && \
	chmod +x /usr/sbin/ruby_config.sh && \
        bash -x /usr/sbin/ruby_config.sh

ADD installs.sh /usr/sbin/installs.sh
RUN chmod +x /usr/sbin/installs.sh && \
	bash -x /usr/sbin/installs.sh

ADD application.sh /usr/sbin/application.sh
RUN chmod +x /usr/sbin/application.sh && \
	bash -x /usr/sbin/application.sh

ADD rails.sh /usr/sbin/rails.sh
RUN chmod +x /usr/sbin/rails.sh

ADD sidekiq.sh /usr/sbin/sidekiq.sh
RUN chmod +x /usr/sbin/sidekiq.sh

COPY supervisord.conf /etc/supervisor.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-n", "-c/etc/supervisor.d/supervisord.conf"]

ENV container docker
ENV DATE_TIMEZONE UTC
VOLUME /var/log /etc
EXPOSE 3000 22
USER root
