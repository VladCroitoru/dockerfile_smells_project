FROM grow/base:master

# Install deps.
RUN apt-get update
RUN apt-get install -y --no-install-recommends libfontconfig

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install globals.
RUN yarn global add firebase-tools

# Fix file ownership.
RUN chown -R root:root /usr/local/share/
