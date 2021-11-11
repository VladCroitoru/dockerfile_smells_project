FROM mattsch/fedora-rpmfusion:latest
MAINTAINER Matthew Schick <matthew.schick@gmail.com>

# Run updates
RUN dnf upgrade -yq && \
    dnf clean all

# Install required packages
RUN dnf install -yq git \
                    python \
                    python2-lxml && \
    dnf clean all

# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the
# default first uid/gid on a fresh Fedora install
ENV LUID=1000 LGID=1000

# Create the nzbhydra user/group
RUN groupadd -g $LGID nzbhydra && \
    useradd -c 'NZBHydra User' -s /bin/bash -m -d /opt/nzbhydra -g $LGID -u $LUID nzbhydra
    
# Grab the installer, do the thing
RUN git clone -q https://github.com/theotherp/nzbhydra.git /opt/nzbhydra/app && \
    chown -R nzbhydra:nzbhydra /opt/nzbhydra

# Need a config and storage volume, expose proper port
VOLUME /config
EXPOSE 5075

# Add script to copy default config if one isn't there and start nzbhydra
COPY run-nzbhydra.sh /bin/run-nzbhydra.sh
 
# Run our script
CMD ["/bin/run-nzbhydra.sh"]


