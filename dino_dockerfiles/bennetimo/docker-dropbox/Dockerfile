FROM debian:jessie

MAINTAINER Tim Bennett

# Install Python
RUN \
  apt-get update && \
  apt-get install -y python wget

# Download and extract dropbox
RUN cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose the Dropbox directory
VOLUME /root/Dropbox

# Setup the Dropbox CLI
ADD https://www.dropbox.com/download?dl=packages/dropbox.py /bin/dropbox.py
RUN chmod 755 /bin/dropbox.py

# Start the Dropbox daemon
CMD /root/.dropbox-dist/dropboxd