FROM jpazdyga/centos7-base
MAINTAINER Jakub Pazdyga <jakub.pazdyga@ft.com>

ENV AWS_ACCESS_KEY XXXX
ENV AWS_SECRET_ACCESS_KEY XXXXXXXX
ENV container docker
ENV DATE_TIMEZONE UTC

RUN rpmdb --rebuilddb && \ 
    rpmdb --initdb && \
    yum clean all && \
    yum -y update && \
    yum -y install wget \ 
		   curl \
		   bind-utils \
		   screen \
		   python \
		   python-devel \
		   python-psycopg2 \
		   python-crypto \
		   nginx \
		   postgresql-server \
		   libffi-devel \
		   openssl-devel \
		   libpqxx-devel \
		   gcc \
		   postgresql \
		   libpqxx-devel \
		   openssh \
                   openssl \ 
                   openssl-libs \
                   psmisc \
                   openssh-server \
                   PyYAML \
                   git \
		   httpd \
		   swig \
		   unzip \
		   python-setuptools \
                   python-pip

RUN pip install --upgrade pip && \
      pip install --upgrade setuptools && \
      easy_install PyYAML

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
RUN mkdir -p /var/log/security_monkey && \
	chown apache:apache /var/log/security_monkey && \
	mkdir -p /var/www && \
	chown apache /var/www && \
	touch /var/log/security_monkey/security_monkey.error.log && \
	touch /var/log/security_monkey/security_monkey.access.log && \
	touch /var/log/security_monkey/security_monkey-deploy.log && \
	chown apache /var/log/security_monkey/security_monkey-deploy.log && \
	runuser -l postgres -c '/usr/bin/initdb --pgdata=/var/lib/pgsql/data --auth=ident'

ADD pgsetup.sh /usr/sbin/pgsetup.sh
RUN runuser -l postgres -c '/usr/bin/postgres -D /var/lib/pgsql/data -p 5432 &' && \
	sleep 10; ps ax | grep postgres && \
	chmod +x /usr/sbin/pgsetup.sh && \
	bash -x /usr/sbin/pgsetup.sh 

ADD smsetup.sh /usr/sbin/smsetup.sh
RUN chmod +x /usr/sbin/smsetup.sh && \
	bash -x /usr/sbin/smsetup.sh

ADD dartsetup.sh /usr/sbin/dartsetup.sh
RUN chmod +x /usr/sbin/dartsetup.sh && \
	mkdir -p /usr/local/src/security_monkey/security_monkey/static/ && \
	bash -x /usr/sbin/dartsetup.sh

ADD secmonkey_config.sh /usr/sbin/secmonkey_config.sh
RUN chmod +x /usr/sbin/secmonkey_config.sh && \
        bash -x /usr/sbin/secmonkey_config.sh

ADD nginxsetup.sh /usr/sbin/nginxsetup.sh
ADD securitymonkey.conf /etc/nginx/sites-available/securitymonkey.conf
RUN mkdir -p /etc/ssl/private && \
	chmod +x /usr/sbin/nginxsetup.sh && \
        bash -x /usr/sbin/nginxsetup.sh

ADD sm_scheduler.sh /usr/sbin/sm_scheduler.sh
ADD sm_api_server.sh /usr/sbin/sm_api_server.sh
ADD botocfg.sh /usr/sbin/botocfg.sh
RUN chmod +x /usr/sbin/sm_scheduler.sh && chmod +x /usr/sbin/sm_api_server.sh && chmod +x /usr/sbin/botocfg.sh && bash -x /usr/sbin/botocfg.sh
RUN echo -e "export PYTHONPATH=\"/usr/local/src/security_monkey\"\nexport SECURITY_MONKEY_SETTINGS=\"/usr/local/src/security_monkey/env-config/config-deploy.py\"" > /usr/sbin/sm_environment.env
COPY supervisord.conf /etc/supervisor.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-n", "-c/etc/supervisor.d/supervisord.conf"]

ENV container docker
ENV DATE_TIMEZONE UTC
VOLUME /var/log /etc
EXPOSE 5432 22 443 80
USER root
