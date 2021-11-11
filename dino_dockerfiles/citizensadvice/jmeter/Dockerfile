FROM java:openjdk-8-jre

RUN apt-get update && \
    apt-get upgrade -y && \
    cd /opt && \
    wget -c http://apache.mirror.anlx.net//jmeter/binaries/apache-jmeter-3.1.tgz && \
    tar xzf apache-jmeter-3.1.tgz && \
    rm apache-jmeter-3.1.tgz && \
    mv apache-jmeter-3.1 jmeter && \
    ln -s /opt/jmeter/bin/jmeter /usr/bin/jmeter && \
    ln -s /opt/jmeter/bin/jmeter-server /usr/bin/jmeter-server && \
    rm -rf /var/lib/apt/lists/*
