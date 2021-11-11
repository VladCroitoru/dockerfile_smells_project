# ubuntu 16.04 with awscli, git, node, npm, openjdk8, mvn and firefox45 installed
FROM ubuntu:16.04
# install dependencies
RUN apt-get update && \
    apt-get install -y \
        software-properties-common \
        build-essential \
        wget \
        xvfb \
        curl \
        git \
        maven \
        python-pip \
        openjdk-8-jdk && \
    # install awscli
    pip install awscli && \
    # install npm 5.6.0 and node 8.x
    curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh && \
    apt-get install -y nodejs && \
    rm nodesource_setup.sh && \
    # install firefox 45
    mkdir /usr/bin/firefox && \
    wget -q --continue --output-document /usr/bin/firefox/firefox.tar.bz2 "https://ftp.mozilla.org/pub/firefox/releases/45.0/linux-x86_64/en-US/firefox-45.0.tar.bz2" && \
    tar -xaf "/usr/bin/firefox/firefox.tar.bz2" --strip-components=1 --directory "/usr/bin/firefox" && \
    # cleanup
    rm -rf /var/lib/apt/lists/*
ENV DISPLAY=:99
ENV PATH /usr/bin/firefox:$PATH
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
WORKDIR /repo/ci
CMD ./build.sh ${build_id}
