# ------------------------------------------------------------------------------
# Based on a work at https://github.com/docker/docker.
# ------------------------------------------------------------------------------
# Pull base image.
FROM ubuntu:14.04
MAINTAINER Alan Scherger <flyinprogrammer@gmail.com>

# ------------------------------------------------------------------------------
# Install base
RUN apt-get update
RUN apt-get install -y build-essential g++ curl libssl-dev apache2-utils git libxml2-dev sshfs

# ------------------------------------------------------------------------------
# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs python

# ------------------------------------------------------------------------------
# Install Cloud9
RUN git clone https://github.com/c9/core.git /cloud9
WORKDIR /cloud9
RUN scripts/install-sdk.sh

# Tweak standlone.js conf
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js

# ------------------------------------------------------------------------------
# Install DVM (for docker client)
RUN curl -sL https://download.getcarina.com/dvm/latest/install.sh | sh
RUN /bin/bash -c "source /root/.dvm/dvm.sh && dvm install 1.9.1 && ln -s /root/.dvm/bin/docker/1.9.1/docker /usr/bin/docker"

# ------------------------------------------------------------------------------
# Install Carina
RUN curl -L https://download.getcarina.com/carina/latest/$(uname -s)/$(uname -m)/carina -o /usr/bin/carina && chmod u+x /usr/bin/carina

# ------------------------------------------------------------------------------
# Add Entrypoint
ADD entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh

# ------------------------------------------------------------------------------
# Add volumes
RUN mkdir /workspace
VOLUME /workspace

# ------------------------------------------------------------------------------
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# ------------------------------------------------------------------------------
# Expose ports.
EXPOSE 80
EXPOSE 3000

CMD ["/entrypoint.sh"]
