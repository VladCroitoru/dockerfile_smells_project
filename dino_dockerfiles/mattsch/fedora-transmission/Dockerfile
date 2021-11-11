FROM mattsch/fedora-rpmfusion:latest
MAINTAINER Matthew Schick <matthew.schick@gmail.com>

# Run updates
RUN dnf upgrade -yq && \
    dnf clean all

# Install required packages
RUN dnf install -yq transmission-daemon && \
    dnf clean all

# Set uid/gid (override with the '-e' flag), 1000/1000 used since it's the
# default first uid/gid on a fresh Fedora install
ENV LUID=1000 LGID=1000

# Add script to copy default config if one isn't there and start transmission
COPY run-transmission.sh /bin/run-transmission.sh
 
# Run our script
CMD ["/bin/run-transmission.sh"]


