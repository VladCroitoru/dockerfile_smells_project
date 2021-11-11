FROM centos

ENV	UPDATE_VERSION=8u66
ENV	JAVA_VERSION=1.8.0_66
ENV	BUILD=b17

RUN	yum -y update && \
	yum -y install wget && \
	wget -c --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/${UPDATE_VERSION}-${BUILD}/jdk-${UPDATE_VERSION}-linux-x64.rpm" --output-document="jdk-${UPDATE_VERSION}-linux-x64.rpm" && \
	rpm -i jdk-${UPDATE_VERSION}-linux-x64.rpm && \
	alternatives --install /usr/bin/java java /usr/java/jdk${JAVA_VERSION}/bin/java 1 && \
	alternatives --set java /usr/java/jdk${JAVA_VERSION}/bin/java && \
	update-alternatives --install /usr/bin/jps jps /usr/java/jdk${JAVA_VERSION}/bin/jps 1 && \
	export JAVA_HOME=/usr/java/jdk${JAVA_VERSION}/ && \
	echo "export JAVA_HOME=/usr/java/jdk${JAVA_VERSION}/" | tee /etc/environment && \
	source /etc/environment && \
	rm jdk-${UPDATE_VERSION}-linux-x64.rpm

ENV	JAVA_HOME=/usr/java/jdk${JAVA_VERSION}/
ENV HOME /root

WORKDIR /root

CMD ["bash"]
