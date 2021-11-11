FROM mattsch/fedora-rpmfusion:28
LABEL maintainer="Matthew Schick <matthew.schick@gmail.com>"
ARG upstream_tag=20.0

# Run updates
RUN dnf upgrade -yq && \
    dnf clean all

# Install required packages
RUN dnf install -yq procps-ng \
                    python \
                    tar \
                    unrar && \
    dnf clean all

# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the
# default first uid/gid on a fresh Fedora install
ENV LUID=1000 LGID=1000 URL="http://github.com/nzbget/nzbget/releases/download"

# Create the nzbget user/group
RUN groupadd -g $LGID nzbget && \
    useradd -c 'NZBGet User' -s /bin/bash -m -d /opt/nzbget -g $LGID -u $LUID nzbget

# Grab the installer, do the thing
RUN cd /tmp && \
    curl -qOL ${URL}/v${upstream_tag/-testing/}/nzbget-$upstream_tag-bin-linux.run && \
    sh ./nzbget-${upstream_tag}-bin-linux.run --destdir /opt/nzbget && \
    rm ./nzbget-${upstream_tag}-bin-linux.run && \
    chown -R nzbget:nzbget /opt/nzbget

# Need a config and storage volume, expose proper port
VOLUME /config /storage
EXPOSE 6789

# Add script to copy default config if one isn't there and start nzbget
COPY run-nzbget.sh /bin/run-nzbget.sh

# Run our script
CMD ["/bin/run-nzbget.sh"]
