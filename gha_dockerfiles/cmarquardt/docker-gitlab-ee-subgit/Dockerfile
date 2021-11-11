FROM gitlab/gitlab-ee:latest
MAINTAINER Christian Marquardt

# Subgit version
ENV SUBGIT_VERSION 3.3.6

# Install Java
RUN apt-get update && \
    apt-get install -y openjdk-8-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/*

# Download subgit from official website and install
RUN curl -o subgit.deb -q https://subgit.com/files/subgit_${SUBGIT_VERSION}_all.deb && \
    dpkg -i subgit.deb && \
    rm -fr subgit.deb

# Fix SNI error with Java 7
RUN sed -i '/^EXTRA_JVM_ARGUMENTS.*/a EXTRA_JVM_ARGUMENTS="$EXTRA_JVM_ARGUMENTS -Djsse.enableSNIExtension=false"' /usr/bin/subgit

# Our wrapper script (enabling cron, and then launching GitLab's wrapper)
COPY assets/outerwrapper /assets/

# Define data volumes
VOLUME ["/etc/gitlab", "/etc/subgit", "/etc/cron.d", "/var/opt/gitlab", "/var/log/gitlab"]

# Wrapper to handle signal, trigger runit and reconfigure GitLab
CMD ["/assets/outerwrapper"]
