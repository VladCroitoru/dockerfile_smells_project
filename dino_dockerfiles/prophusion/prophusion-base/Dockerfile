FROM ubuntu:14.04
MAINTAINER Mike Baynton <mike@mbaynton.com>

RUN apt-get update

# install curl
RUN apt-get install -y curl git && apt-get clean

# install a few libraries php pretty much always should have
RUN apt-get install -y libxml2 libssl-dev libxslt1.1 libtidy-0.99-0 libmcrypt4 libjpeg8 libicu52 && apt-get clean

# install phpenv
ENV PHPENV_ROOT /usr/local/phpenv
RUN curl https://raw.githubusercontent.com/CHH/phpenv/master/bin/phpenv-install.sh | bash

# Setup $PATH for phpenv and the php binaries the system should be finding.
RUN echo 'export PATH="/usr/local/phpenv/bin:$PATH"' > /etc/bash.bashrc.phpenv_setup \
 && echo 'eval "$(phpenv init -)"' >> /etc/bash.bashrc.phpenv_setup \
 && echo '. /etc/bash.bashrc.phpenv_setup' >> /etc/bash.bashrc

# Make the location of the php environments a volume
VOLUME /usr/local/phpenv/versions

# RUN ["/bin/bash", "-c", "source /etc/bash.bashrc.phpenv_setup"]

# Make a place to unpack php builds before we have verified their hashes
RUN mkdir /usr/local/phpenv/versions/.unverified
RUN ["/bin/bash", "-c", "chmod a+rwx -R /usr/local/phpenv/versions"]

# Install prophusion script
COPY prophusion.sh /usr/local/phpenv/bin/prophusion
# Install xdebug2host script
COPY xdebug2host.sh /usr/local/bin/xdebug2host

# Make a link in /usr/local/bin. This makes it easier to run `docker exec [container] prophusion ...` from the host.
RUN ln -s /usr/local/phpenv/bin/prophusion /usr/local/bin/prophusion

COPY prophusion-base-entrypoint.sh /prophusion-base-entrypoint.sh
ENTRYPOINT ["/prophusion-base-entrypoint.sh"]
