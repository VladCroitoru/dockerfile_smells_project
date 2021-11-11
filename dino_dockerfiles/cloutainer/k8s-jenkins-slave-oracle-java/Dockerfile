FROM cloutainer/k8s-jenkins-slave-base:v24

#
# USER: super
#
USER root

#
# ATLASSIAN SDK
#
ENV ATLS_VERSIN 8.2.6
RUN curl -jkSL -o /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz \
    https://packages.atlassian.com/maven/repository/public/com/atlassian/amps/atlassian-plugin-sdk/${ATLS_VERSIN}/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz && \
    tar -C /opt -xf /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz && \
    chown -R jenkins:root /opt/atlassian-plugin-sdk-${ATLS_VERSIN} && \
    rm -f /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz

#
# ORACLE OPENJDK JAVA
#
RUN curl -jkSL -o /opt/jdk-linux-x64.tar.gz \
    #"https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u222-b10/OpenJDK8U-jdk_x64_linux_hotspot_8u222b10.tar.gz" && \
    # github releases are super slow ... so using other mirror
    "https://ftp.fau.de/gentoo/distfiles/OpenJDK8U-jdk_x64_linux_hotspot_8u282b08.tar.gz" && \
    tar -C /opt -xf /opt/jdk-linux-x64.tar.gz && \
    ls -lah /opt && \
    mv /opt/jdk8u282* /opt/jdk && \
    rm -f /opt/jdk-linux-x64.tar.gz && \
    chown jenkins /opt/jdk/lib/security/cacerts | true && \
    chown jenkins /opt/jdk/jre/lib/security/cacerts | true && \
    update-alternatives --install "/usr/bin/java" "java" "/opt/jdk/bin/java" 1 && \
    update-alternatives --install "/usr/bin/javac" "javac" "/opt/jdk/bin/javac" 1 && \
    #update-alternatives --install "/usr/bin/javaws" "javaws" "/opt/jdk/bin/javaws" 1 && \
    update-alternatives --install "/usr/bin/jar" "jar" "/opt/jdk/bin/jar" 1 && \
    update-alternatives --set "java" "/opt/jdk/bin/java" && \
    update-alternatives --set "javac" "/opt/jdk/bin/javac" && \
    #update-alternatives --set "javaws" "/opt/jdk/bin/javaws" && \
    update-alternatives --set "jar" "/opt/jdk/bin/jar"

#
# APACHE MAVEN
#
RUN curl -jkSL -o /opt/maven.tar.gz https://www-eu.apache.org/dist/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz && \
    tar -C /opt -xf /opt/maven.tar.gz && \
    rm -f /opt/maven.tar.gz && \
    mv /opt/apache-maven-* /opt/apache-maven/

#
# GRADLE
#
RUN curl -jkSL -o /opt/gradle.zip https://services.gradle.org/distributions/gradle-6.8.2-bin.zip && \
    unzip /opt/gradle.zip -d /opt/ && \
    rm -f /opt/gradle.zip && \
    mv /opt/gradle-* /opt/gradle/


#
# KUBERNETES CLI (kubectl)
#
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl

#
# INSTALL AND CONFIGURE
#
COPY docker-entrypoint-hook.sh /opt/docker-entrypoint-hook.sh
RUN chmod u+rx,g+rx,o+rx,a-w /opt/docker-entrypoint-hook.sh

#
# USER: normal
#
USER jenkins

#
# RUN
#
ENV JAVA_HOME /opt/jdk
ENV PATH ${PATH}:/opt/atlassian-plugin-sdk-${ATLS_VERSIN}/bin/:/opt/jdk/bin:/opt/gradle/bin:/opt/apache-maven/bin
USER jenkins
