FROM jotadrilo/watchman:latest
MAINTAINER Joseda <josriolop@gmail.com>

ENV IMAGE_NUCLIDE_VERSION=0.205.0 \
    HOME=/root

# Install SSH server
RUN install_packages openssh-server && mkdir /var/run/sshd

# SSHD scrubs the environment
# http://stackoverflow.com/questions/36292317/why-set-visible-now-in-etc-profile
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Install Node.js
RUN install_packages curl ca-certificates && \
    curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
    install_packages nodejs

# Install Nuclide Remote Server
RUN npm install -g nuclide@${IMAGE_NUCLIDE_VERSION} && \
    rm -rf /root/.npm/*

COPY rootfs /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
