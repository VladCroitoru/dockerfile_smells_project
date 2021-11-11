FROM mattsch/fedora-rpmfusion:29
LABEL maintainer="Matthew Schick <matthew.schick@gmail.com>"
ARG upstream_tag=2.0.0.5252

# Run updates
RUN dnf upgrade -yq && \
    dnf clean all

# Add copr
COPY tpokorra-mono-fedora.repo /etc/yum.repos.d/

# Install required packages
RUN dnf install -yq mediainfo \
                    mono-core \
                    procps-ng \
                    shadow-utils \
                    tar \
                    unrar && \
    dnf clean all

# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the
# default first uid/gid on a fresh Fedora install
ENV LUID=1000 LGID=1000

# Create the sonarr user/group
RUN groupadd -g $LGID sonarr && \
    useradd -c 'Sonarr User' -s /bin/bash -m -d /opt/sonarr -g $LGID -u $LUID sonarr

# Grab the installer, do the thing
RUN cd /opt && \
    curl -sL -o - \
        http://download.sonarr.tv/v2/master/mono/NzbDrone.master.${upstream_tag}.mono.tar.gz \
        | tar xzf - && \
    chown -R sonarr:sonarr /opt/NzbDrone

# Need a config and storage volume, expose proper port
VOLUME /config /storage
EXPOSE 8989

# Add script to copy default config if one isn't there and start sonarr
COPY run-sonarr.sh update-sonarr.sh /bin/

# Run our script
CMD ["/bin/run-sonarr.sh"]

