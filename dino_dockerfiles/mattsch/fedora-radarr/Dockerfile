FROM mattsch/fedora-rpmfusion:28
LABEL maintainer="Matthew Schick <matthew.schick@gmail.com>"
ARG upstream_tag=v0.2.0.995

# Run updates
RUN dnf upgrade -yq && \
    dnf clean all

# Add copr
COPY tpokorra-mono-fedora.repo /etc/yum.repos.d/

# Install required packages
RUN dnf install -yq mediainfo \
                    mono-core \
                    mono-locale-extras \
                    procps-ng \
                    shadow-utils \
                    tar \
                    unrar && \
    dnf clean all

# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the
# default first uid/gid on a fresh Fedora install
ENV LUID=1000 LGID=1000 URL="https://github.com/galli-leo/Radarr/releases/download"

# Create the radarr user/group
RUN groupadd -g $LGID radarr && \
    useradd -c 'Radarr User' -s /bin/bash -m -d /opt/Radarr \
    -g $LGID -u $LUID radarr

# Grab the installer, do the thing
RUN cd /opt && \
    curl -sL -o - \
        ${URL}/${upstream_tag}/Radarr.develop.${upstream_tag#v}.linux.tar.gz \
        | tar -xzf - && \
    chown -R radarr:radarr /opt/Radarr

# Need a config and storage volume, expose proper port
VOLUME /config /storage
EXPOSE 7878

# Add script to copy default config if one isn't there and start radarr
COPY run-radarr.sh update-radarr.sh /bin/

# Run our script
CMD ["/bin/run-radarr.sh"]
