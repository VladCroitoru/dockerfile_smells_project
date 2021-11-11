# Dockerfile used to build base image for projects using Python, Node, and Ruby.
FROM phusion/baseimage:0.9.17
MAINTAINER Tim Zenderman <tim@bananadesk.com>
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile

WORKDIR /code

ENV NVM_DIR /usr/local/nvm
ENV PATH $NVM_DIR/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH


# Install nvm and default node version.
COPY .nvmrc /code/.nvmrc
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.23.3/install.sh | bash && \
    echo 'source $NVM_DIR/nvm.sh' >> /etc/profile && \
    /bin/bash -l -c "nvm install;" \
    "nvm use;"

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
