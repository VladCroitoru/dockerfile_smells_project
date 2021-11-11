FROM ubuntu:xenial

RUN apt-get update

# Add the duplicity-team repo to get up to date version
RUN apt-get install -y software-properties-common python-software-properties git-core
RUN add-apt-repository ppa:duplicity-team/ppa

# Install duplicity
RUN apt-get update
RUN apt-get install -y duplicity python-setuptools
RUN apt-get install -y python3 python3-appdirs python3-dateutil python3-requests \
                       python3-sqlalchemy python3-pip python-setuptools python-boto \
                       python-swiftclient python-pexpect openssh-client

# Install acd_cli for duplicity to use
RUN pip3 install --upgrade git+https://github.com/yadayada/acd_cli.git

# Cleanup

RUN apt-get -y purge git-core
RUN apt-get -y autoremove --purge
RUN rm -rf /var/apt/lists/*

# Expecting both duplicity and acd_cli subdirs here
VOLUME [ "/root/.cache" ]

ENTRYPOINT [ "duplicity" ]
CMD [ "--help" ]