FROM ubuntu:16.04

MAINTAINER André Stein

EXPOSE 80
EXPOSE 443

VOLUME /data

# seafile version updates here
# make sure that SEAFILE_MAJOR matches SEAFILE_VERSION!
# additional the seafile versions may be passed as --build-arg variables
# thus overriding this default!
ARG SEAFILE_VERSION=6.2.3
ENV SEAFILE_VERSION ${SEAFILE_VERSION}
ARG SEAFILE_MAJOR=6.2
ENV SEAFILE_MAJOR ${SEAFILE_MAJOR}

# Install seafile dependencies and make sure to clean
# all apt caches
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q --fix-missing && \
	apt-get -y install python wget nginx && \
	apt-get -y install python2.7 libpython2.7 python-setuptools python-imaging python-ldap python-urllib3 sqlite3 && \
	apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
	rm -rf /usr/share/locale/* && rm -rf /usr/share/man/* && rm -rf /usr/share/doc/*

# download and extract seafile release
RUN mkdir seafile && cd /seafile && \
	wget -O - https://download.seadrive.org/seafile-server_${SEAFILE_VERSION}_x86-64.tar.gz | tar xzvf -

# run initial seafile setup script with initial placeholder
# values which will be patched in the container start script
RUN cd /seafile/seafile-server-* && ./setup-seafile.sh auto \
	-n "xxxseafilexxx" \
	-i 000.000.000.000

ADD target/start-seafile.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start-seafile.sh

# patch seahub's check_init_admin.py script which tries to
# interactively set admin's mail and password. We directly
# patch it to use environment variables
RUN sed -i 's/= ask_admin_email()/= os\.environ\["SEAFILE_ADMIN_MAIL"\]/' /seafile/seafile-server-latest/check_init_admin.py
RUN sed -i 's/= ask_admin_password()/= os\.environ\["SEAFILE_ADMIN_PASSWORD"\]/' /seafile/seafile-server-latest/check_init_admin.py

# patch seafile's update scripts to be non-interactive
RUN sed -i 's@read dummy@@g' /seafile/seafile-server-latest/upgrade/upgrade_*sh

# setup nginx configuration files
RUN rm /etc/nginx/sites-*/*
COPY target/nginx/seafile-*.conf /etc/nginx/sites-available/
COPY target/nginx/snippets/* /etc/nginx/snippets/

CMD /usr/local/bin/start-seafile.sh
