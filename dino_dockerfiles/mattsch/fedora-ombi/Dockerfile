FROM mattsch/fedora-rpmfusion:28
LABEL maintainer="Matthew Schick <matthew.schick@gmail.com>"
ARG upstream_tag=v3.0.3587

# Run updates
RUN dnf upgrade -yq && \
    dnf clean all

# Install required packages
RUN dnf install -yq compat-openssl10 \
                    curl \
                    libicu \
                    libunwind \
                    procps-ng \
                    shadow-utils \
                    tar && \
    dnf clean all

# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the
# default first uid/gid on a fresh Fedora install
ENV LUID=1000 LGID=1000

# Create the plexreqs user/group
RUN groupadd -g $LGID ombi && \
    useradd -c 'Ombi User' -s /bin/bash -m -d /opt/Ombi \
    -g $LGID -u $LUID ombi

# Grab the installer, do the thing
RUN mkdir -p /opt/Ombi && \
    cd /opt/Ombi && \
    curl -sL -o - \
        https://github.com/tidusjar/Ombi/releases/download/${upstream_tag}/linux.tar.gz \
        | tar xzf - && \
    chown -R ombi:ombi /opt/Ombi

# Need a config and storage volume, expose proper port
VOLUME /config
EXPOSE 5000

# Add script to copy default config if one isn't there and start plexreqs
COPY run-ombi.sh /bin/

# Run our script
CMD ["/bin/run-ombi.sh"]
