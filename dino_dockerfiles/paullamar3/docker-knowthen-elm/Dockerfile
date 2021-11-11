## Dockerfile for creating LaTeX documents.
FROM node
MAINTAINER Paul LaMar <pal3@outlook.com>

# Add utility scripts: p_addpkgs, p_adduser, and gosu
COPY clocal/* /usr/local/bin/
RUN chmod +x /usr/local/bin/*

# Install the packages atom will need.
RUN p_addpkgs git gconf2 gconf-service gvfs-bin libasound2 libgconf-2-4 \
        libgnome-keyring-dev libgtk2.0-0 libnotify4 libnss3 libxtst6 \
        xdg-utils ca-certificates curl

# Install Elm
RUN npm install -g elm

#Install Atom
ENV ATOM_VERSION 1.9.0

RUN curl -sSL https://github.com/atom/atom/releases/download/v${ATOM_VERSION}/atom-amd64.deb -o /tmp/atom-amd64.deb \
    && dpkg -i /tmp/atom-amd64.deb \
    && rm -rf /tmp/*.deb 

# Install language-elm for atom.
RUN apm install language-elm

# Install elm-oracle for Elm.
RUN npm install -g elm-oracle \
    && printf "\"*\":\n    \"language-elm\":\n        elmOraclePath: \"/usr/local/bin/elm-oracle\"\n" > /root/.atom/config.cson \
    && chmod 777 /root/.atom/config.cson

# Download and install the elm-format plugin.
RUN curl -sSL https://github.com/avh4/elm-format/releases/download/0.4.0-alpha/elm-format-0.17-0.4.0-alpha-linux-x64.tgz -o /tmp/elm-format-0.17-0.4.0-alpha-linux-x64.tgz \
   && cd /tmp \
   && tar -xvf elm-format-0.17-0.4.0-alpha-linux-x64.tgz \
   && mv elm-format /usr/local/bin/ \
   && rm elm-format-0.17-0.4.0-alpha-linux-x64.tgz \
   && cd /root \
   && apm install elm-format

# Note that the default configuration for elm-format is fine; no need to 
# modify the config.cson.

# Install the linter and the elm make.
RUN apm install linter \
    && apm install linter-elm-make

# Note that apm does not install globally. We need to move the 
# important files out of /root/.atom into /etc/skel/.atom so that
# the packages installed by root will also be available to new users.
RUN mkdir /etc/skel/.atom \
    && cp -r /root/.atom/packages /etc/skel/.atom/packages \
    && cp -r /root/.atom/.apm /etc/skel/.atom/.apm \
    && cp /root/.atom/config.cson /etc/skel/.atom/

# Copy the entrypoint script.
COPY entrypoint.sh /root/
RUN chmod +x /root/entrypoint.sh

ENTRYPOINT ["/root/entrypoint.sh"]
