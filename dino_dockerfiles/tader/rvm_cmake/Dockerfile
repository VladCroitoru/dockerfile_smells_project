FROM adgud2/ruby-rvm:latest

RUN apt-get update -qqy && apt-get install -qqy \
        awscli \
        build-essential \
        cmake \
        colordiff \
        unzip \
        wget \
        zip \
        && rm -rf /var/lib/apt/lists

RUN cd /tmp \
        ; wget https://releases.hashicorp.com/packer/0.12.2/packer_0.12.2_linux_amd64.zip \
        ; wget http://stedolan.github.io/jq/download/linux64/jq \
        ; unzip *.zip \
        ; install -t /usr/bin -g root -o root -m 0755 /tmp/packer* /tmp/jq \
        ; rm -f /tmp/*.zip /tmp/packer* /tmp/jq

ENV ADDITIONAL_RUBIES "2.1.0 2.2.3 2.2.5"
RUN /bin/bash -l -c 'for version in $ADDITIONAL_RUBIES; do echo "Now installing Ruby $version"; rvm install $version; rvm cleanup sources; done'

