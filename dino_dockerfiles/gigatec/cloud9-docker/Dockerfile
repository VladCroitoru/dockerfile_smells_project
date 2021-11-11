# ------------------------------------------------------------------------------
# Based on a work at https://github.com/kdelfour/cloud9-docker..
# ------------------------------------------------------------------------------

# Pull base image.
FROM ubuntu:14.04

MAINTAINER Stefan Kreuter <kreuter@gigatec.de>

# Install Supervisor.
RUN apt-get update && apt-get install -y supervisor && sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

# Define mountable directories.
VOLUME ["/etc/supervisor/conf.d"]

# ------------------------------------------------------------------------------
# Security changes
# - Determine runlevel and services at startup [BOOT-5180]
RUN update-rc.d supervisor defaults

# - Check the output of apt-cache policy manually to determine why output is empty [KRNL-5788]
#RUN apt-get update | apt-get upgrade -y

# - Install a PAM module for password strength testing like pam_cracklib or pam_passwdqc [AUTH-9262]
RUN apt-get update && apt-get install libpam-cracklib -y && ln -s /lib/x86_64-linux-gnu/security/pam_cracklib.so /lib/security

# Define working directory.
WORKDIR /etc/supervisor/conf.d

# ------------------------------------------------------------------------------
# Start supervisor, define default command.
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

# ------------------------------------------------------------------------------
# Install base
RUN apt-get update && apt-get install -y build-essential g++ curl libssl-dev apache2-utils git libxml2-dev sshfs

# ------------------------------------------------------------------------------
# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup | bash - && apt-get update && apt-get install -y nodejs
    
# ------------------------------------------------------------------------------
# Force Dockerfile rebuild (set cloud9-docker.version)
RUN echo 0.2 > /cloud9-docker.version
    
# ------------------------------------------------------------------------------
# Install Cloud9
RUN git clone https://github.com/c9/core.git /cloud9
WORKDIR /cloud9
RUN scripts/install-sdk.sh

# Tweak standlone.js conf
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js 

# Add supervisord conf
ADD conf/cloud9.conf /etc/supervisor/conf.d/

# Install Codeintel
RUN apt-get update && apt-get install -y python-pip python-dev \
	&& pip install -U pip \
	&& pip install -U virtualenv \
	&& virtualenv --python=python2 $HOME/.c9/python2 \
	&& . $HOME/.c9/python2/bin/activate \
	&& mkdir /tmp/codeintel \
	&& pip download -d /tmp/codeintel codeintel==0.9.3 \
	&& cd /tmp/codeintel \
	&& tar xf CodeIntel-0.9.3.tar.gz \
	&& mv CodeIntel-0.9.3/SilverCity CodeIntel-0.9.3/silvercity \
	&& tar czf CodeIntel-0.9.3.tar.gz CodeIntel-0.9.3 \
	&& pip install -U --no-index --find-links=/tmp/codeintel codeintel 
	
RUN apt-get update \
    && apt-get install -y php5-dev php5-mysql php5-xdebug sudo mysql-server \
    && mkdir -p /etc/php5/mods-available \
    && echo "xdebug.remote_enable=1" >> /etc/php5/mods-available/xdebug.ini \
    && php5enmod xdebug

# ------------------------------------------------------------------------------
# Add volumes
RUN mkdir /workspace
VOLUME /workspace

# ------------------------------------------------------------------------------
# Expose ports.
EXPOSE 80
EXPOSE 3000

# ------------------------------------------------------------------------------
# Start supervisor, define default command.
#CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

RUN mv /root /home/dev && chmod -R 777 /home/dev && ln -s /home/dev /root

COPY ./entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
