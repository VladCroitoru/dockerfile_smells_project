# vim:set ft=dockerfile:
FROM centos:latest 

# Install required packages 
RUN yum install -y bc java-1.8.0-openjdk openssh-clients rsync tar unzip && \
    yum localinstall -y https://dl.fedoraproject.org/pub/epel/6/x86_64/stress-1.0.4-4.el6.x86_64.rpm && \
    yum clean all

# Setup jmeter
RUN mkdir -p /opt/jmeter && \
    curl -Ls http://mirrors.gigenet.com/apache/jmeter/binaries/apache-jmeter-3.0.tgz \
	| tar xz --strip=1 -C /opt/jmeter && \
        echo "jmeter.save.saveservice.url=true" >> /opt/jmeter/bin/jmeter.properties && \
        echo "jmeter.save.saveservice.thread_counts=true" >> /opt/jmeter/bin/jmeter.properties && \
	echo "jmeter.save.saveservice.autoflush=true" >> /opt/jmeter/bin/user.properties && \
	ln -s /opt/jmeter/bin/jmeter.sh /usr/bin/jmeter

# Setup slstress
WORKDIR /usr/local/bin
RUN curl -Ls https://raw.githubusercontent.com/jmencak/perf-tools/master/bin/x86-64/slstress -O \
             https://raw.githubusercontent.com/jmencak/perf-tools/master/slstress_go/logger.sh -O \
             && chmod 755 ./slstress ./logger.sh

WORKDIR /opt/jmeter
COPY JMeterPlugins-Standard-1.4.0.zip JMeterPlugins-Extras-1.4.0.zip docker-entrypoint.sh test.jmx ./
RUN unzip -n \*.zip && \
    rm *.zip

CMD ["./docker-entrypoint.sh"]
