FROM mattsch/fedora-rpmfusion:28
LABEL maintainer="Matthew Schick <matthew.schick@gmail.com>"
ARG upstream_tag=v2.0.1

# Install required packages
RUN dnf install -yq java-1.8.0-openjdk-headless \
                    python \
                    unzip && \
    dnf clean all

# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the
# default first uid/gid on a fresh Fedora install
ENV LUID=1000 LGID=1000

# Create the nzbhydra user/group
RUN groupadd -g $LGID nzbhydra2 && \
    useradd -c 'NZBHydra2 User' -s /bin/bash -m -d /opt/nzbhydra2 -g $LGID -u \
    $LUID nzbhydra2

# Grab the installer, do the thing
RUN cd /tmp && \
    curl -qsSL -o /tmp/nzbhydra2.zip \
    https://github.com/theotherp/nzbhydra2/releases/download/${upstream_tag}/nzbhydra2-${upstream_tag#v}-linux.zip && \
    mkdir -p /opt/nzbhydra2 && \
    cd /opt/nzbhydra2 && \
    unzip -q /tmp/nzbhydra2.zip && \
    rm /tmp/nzbhydra2.zip && \
    chmod +x /opt/nzbhydra2/nzbhydra2

# Need a config and storage volume, expose proper port
VOLUME /config
EXPOSE 5076

# Add script to copy default config if one isn't there and start nzbhydra
COPY run-nzbhydra2.sh /bin/run-nzbhydra2.sh

# Run our script
CMD ["/bin/run-nzbhydra2.sh"]
