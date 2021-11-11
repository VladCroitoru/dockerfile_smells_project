FROM mattsch/fedora-rpmfusion:28
LABEL maintainer="Matthew Schick <matthew.schick@gmail.com>"
ARG upstream_tag=v2.0.20-beta

# Run updates
RUN dnf upgrade -yq && \
    dnf clean all

# Install required packages
RUN dnf install -yq curl \
                    gcc \
                    git \
                    gmp \
                    python \
                    python-devel \
                    redhat-rpm-config \
                    which && \
    pip install -q pycryptodomex && \
    dnf remove -yq gcc \
                   python-devel \
                   redhat-rpm-config && \
    dnf clean all

# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the
# default first uid/gid on a fresh Fedora install
ENV LUID=1000 LGID=1000

# Create the plexpy user/group
RUN groupadd -g $LGID tautulli && \
    useradd -c 'Tautulli User' -s /bin/bash -m -d /opt/tautulli \
        -g $LGID -u $LUID tautulli

# Grab the installer, do the thing
RUN cd /opt/tautulli && \
    git clone -q https://github.com/Tautulli/Tautulli.git app \
        -b ${upstream_tag} --depth 1 && \
    chown -R tautulli:tautulli /opt/tautulli

# Need a config and storage volume, expose proper port
VOLUME /config
EXPOSE 8181

# Add script to copy default config if one isn't there and start tautulli
COPY run-tautulli.sh /bin/run-tautulli.sh

# Run our script
CMD ["/bin/run-tautulli.sh"]
