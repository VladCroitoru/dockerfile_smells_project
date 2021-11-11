FROM opensuse:tumbleweed
MAINTAINER Markos Chandras <mchandras@suse.de>

# Set good repos
RUN rm -rf /etc/zypp/repos.d/* && \
zypper -n -q ar -f -c http://download.opensuse.org/tumbleweed/repo/oss repo-oss && \
zypper -n -q ar -f -c http://download.opensuse.org/tumbleweed/repo/non-oss repo-non-oss && \
zypper -n -q ar -f -c http://download.opensuse.org/tumbleweed/repo/debug repo-debug && \
zypper -n -q ar -f -c http://download.opensuse.org/update/tumbleweed/ repo-update

# Update it
RUN zypper ref && zypper -n up

# Install all the needed ruby goodies
RUN zypper -n in yast2 yast2-testsuite \
    yast2-python-bindings \
    yast2-ruby-bindings ruby*-rubygem-rspec* \
    ruby*-rubygem-yast-rake \
    yast2-ycp-ui-bindings-devel \
    automake autoconf make which \
    osc git shadow sudo vim less

# Default user
ENV USER=devuser
ENV HOME /home/${USER}
ENV WORKDIR /home/${USER}

# Fix sudoers file to allow wheel group to do anything
RUN echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

ADD wrap_bash.sh /usr/sbin

ENTRYPOINT ["wrap_bash.sh"]
