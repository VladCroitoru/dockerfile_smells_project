FROM ggtools/busybox-ubuntu
MAINTAINER Christophe Labouisse <christophe@labouisse.org>

ENV JAVA8_UPDATE_NUMBER 51

# Install jre with tools.jar
RUN (curl -s -k -L -C - https://bintray.com/artifact/download/clabouisse/obuildfactory-generic-x86-64/jdk-1.8.0-openjdk-x86_64-1.8.0_u${JAVA8_UPDATE_NUMBER}.tar.xz \
	|  tar -xpoJf -) \
	&& mv /jdk1.8.0_${JAVA8_UPDATE_NUMBER}/jre /jre1.8.0_${JAVA8_UPDATE_NUMBER} \
	&& mv /jdk1.8.0_${JAVA8_UPDATE_NUMBER}/lib/tools.jar /jre1.8.0_${JAVA8_UPDATE_NUMBER}/lib/ext \
	&& mv /jdk1.8.0_${JAVA8_UPDATE_NUMBER}/bin/javac /jre1.8.0_${JAVA8_UPDATE_NUMBER}/bin \
	&& rm -Rf /jdk1.8.0_${JAVA8_UPDATE_NUMBER} \
    && chmod -R go+rX /jre1.8.0_${JAVA8_UPDATE_NUMBER} # Temporary perm fix

ENV JAVA_HOME /jre1.8.0_${JAVA8_UPDATE_NUMBER}
ENV PATH $PATH:$JAVA_HOME/bin

ADD lib /lib

CMD ["java"]
