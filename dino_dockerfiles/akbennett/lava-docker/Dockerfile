FROM debian:jessie-backports

MAINTAINER Alan Bennett <alan.bennett@linaro.org>
LABEL Version="1.1" Description="lava running in docker and ready to run jobs"

# Add services helper utilities to start and stop LAVA
COPY stop.sh .
COPY start.sh .

# Install debian packages used by the container
# Configure apache to run the lava server
RUN echo 'lava-server   lava-server/instance-name string lava-docker-instance' | debconf-set-selections \
 && echo 'locales locales/locales_to_be_generated multiselect C.UTF-8 UTF-8, en_US.UTF-8 UTF-8 ' | debconf-set-selections \
 && echo 'locales locales/default_environment_locale select en_US.UTF-8' | debconf-set-selections \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
 android-tools-fastboot \
 cu \
 expect \
 lava-coordinator \
 lava-dev \
 lava-dispatcher \
 lava-tool \
 linaro-image-tools \
 locales \
 openssh-server \
 postgresql \
 screen \
 sudo \
 vim \
 && service postgresql start \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y -t jessie-backports \
 lava \
 python-sphinx \
 qemu-system-arm \
 qemu-system-x86 \
 && a2enmod proxy proxy_http \
 && a2dissite 000-default \
 && a2ensite lava-server \
 && /stop.sh \
 && rm -rf /var/lib/apt/lists/*

## This is an optional step to install the latest LAVA code
# add some dependencies to support installing latest lava code
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
 docbook-xsl \
 gunicorn \
 python-mock \
 python-sphinx-bootstrap-theme node-uglify \
 xsltproc \
 && rm -rf /var/lib/apt/lists/*

## This is an optional step to install the latest LAVA code
# Build and Install latest LAVA Code from master branch
RUN /start.sh \
 && git clone -b master https://git.linaro.org/lava/lava-dispatcher.git /home/lava/lava-dispatcher \
 && cd /home/lava/lava-dispatcher \
 ## for development, apply patches for lava-dispatcher here \
 && git clone -b master https://git.linaro.org/lava/lava-server.git /home/lava/lava-server \
 && cd /home/lava/lava-server \
 ## for development, apply patches for lava-server here \ 
 && echo "add build then install capability to debian-dev-build.sh" \
 && echo "cd \${DIR} && dpkg -i *.deb" >> /home/lava/lava-server/share/debian-dev-build.sh \
 && echo "Installing dispatcher & server" \
 && cd /home/lava/lava-dispatcher && /home/lava/lava-server/share/debian-dev-build.sh -p lava-dispatcher \
 && cd /home/lava/lava-server && /home/lava/lava-server/share/debian-dev-build.sh -p lava-server \
 && /stop.sh

# (Optional) Add lava user SSH key and/or configuration
# or mount a host file as a data volume (read-only)
# e.g. -v /path/to/id_rsa_lava.pub:/home/lava/.ssh/authorized_keys:ro
#COPY lava-credentials/.ssh /home/lava/.ssh

# Remove comment to enable local proxy server (e.g. apt-cacher-ng)
#RUN echo 'Acquire::http { Proxy "http://dockerproxy:3142"; };' >> /etc/apt/apt.conf.d/01proxy

# Add lava user with super-user privilege
RUN useradd -m -G plugdev lava \
 && echo 'lava ALL = NOPASSWD: ALL' > /etc/sudoers.d/lava \
 && chmod 0440 /etc/sudoers.d/lava \
 && mkdir -p /var/run/sshd /home/lava/bin /home/lava/.ssh \
 && chmod 0700 /home/lava/.ssh \
 && chown -R lava:lava /home/lava/bin /home/lava/.ssh

# (Optional) Add lava user SSH key and/or configuration
# or mount a host file as a data volume (read-only)
# e.g. -v /path/to/id_rsa_lava.pub:/home/lava/.ssh/authorized_keys:ro
#COPY lava-credentials/.ssh /home/lava/.ssh

# Remove comment to enable local proxy server (e.g. apt-cacher-ng)
#RUN echo 'Acquire::http { Proxy "http://dockerproxy:3142"; };' >> /etc/apt/apt.conf.d/01proxy

# Add misc utilities
COPY createsuperuser.sh getAPItoken.sh lava-credentials.txt /home/lava/bin/

# Create a admin user (Insecure note, this creates a default user, username: admin/admin)
RUN /start.sh \
 && /home/lava/bin/createsuperuser.sh \
 && /stop.sh

# To script jobs using python XMLRPC, we need the API token (really ugly scraping)
RUN /start.sh \
 && /home/lava/bin/getAPItoken.sh \
 && /stop.sh

# Add some job submission utilities
COPY submittestjob.sh /home/lava/bin/
COPY *.json *.py *.yaml /home/lava/bin/

# Add misc utilities
COPY qemu.jinja2 /etc/dispatcher-config/devices/

# Add  device creation helpers
COPY add-kvm-to-lava.sh add-qemu-to-lava.sh /home/lava/bin/

EXPOSE 22 80
# add devices after the system starts running to deal with slave/master hostname registration
CMD /start.sh \
 && /home/lava/bin/add-qemu-to-lava.sh 2 \
 && /home/lava/bin/add-kvm-to-lava.sh 2 \
 && /home/lava/bin/submit.py -k /home/lava/bin/apikey.txt /home/lava/bin/kvm-basic.json \
 && /home/lava/bin/submityaml.py -k /home/lava/bin/apikey.txt /home/lava/bin/job1.yaml \
 && bash
# Following CMD option starts the lava container without a shell and exposes the logs
#CMD /start.sh && tail -f /var/log/lava-*/*
