#
# Based on work from kdelfour/cloud9-docker
#
FROM cloud9/ws-default
MAINTAINER j7an <github.com/j7an/cloud9-workspace>

# Install base
RUN apt-get update
RUN apt-get install -y build-essential g++ curl libssl-dev apache2-utils git libxml2-dev sshfs

# Install latest v6 Node.js
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs

# Install Cloud9 as ubuntu user
USER ubuntu
RUN git clone https://github.com/c9/core.git /home/ubuntu/cloud9
WORKDIR /home/ubuntu/cloud9
RUN bash -l -c "scripts/install-sdk.sh"

# Tweak standlone.js conf
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /home/ubuntu/cloud9/configs/standalone.js

# Fix PTY
RUN C9_DIR=$HOME/.c9
RUN PATH="$C9_DIR/node/bin/:$C9_DIR/node_modules/.bin:$PATH"
RUN cd $C9_DIR
RUN bash -l -c "npm install pty.js"

# Clean up APT when done.
USER root
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose ports.
EXPOSE 80
EXPOSE 3000

CMD [ "node", "/home/ubuntu/cloud9/server.js", "--listen", "0.0.0.0", "--port", "80", "-w", "/home/ubuntu" ]