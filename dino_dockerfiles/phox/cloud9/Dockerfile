FROM node:6

# ------------------------------------------------------------------------------
# Install base
RUN apt-get update
RUN apt-get install -y build-essential g++ curl libssl-dev apache2-utils git libxml2-dev sshfs gyp

# Install Cloud9 IDE
RUN git clone git://github.com/c9/core.git /cloud9
WORKDIR /cloud9
RUN scripts/install-sdk.sh

#RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js 
RUN sed -i -e 's_\(^\s\+\)\(user\.save(function(\)_\1user\.save \&\& \2_g' /cloud9/plugins/c9.vfs.server/vfs.server.js

# Declare volume for workspace storage
RUN mkdir /workspace
WORKDIR /workspace
VOLUME ["/workspace"]

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# WebUI
EXPOSE 80
# Node listen port
EXPOSE 3000


# Start container services
CMD /usr/local/bin/node /cloud9/server.js --port 80 -w /workspace --packed --listen 0.0.0.0 -a :
