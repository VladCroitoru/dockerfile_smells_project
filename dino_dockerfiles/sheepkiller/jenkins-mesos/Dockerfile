# Based on https://github.com/jenkinsci/mesos-plugin/
#          https://hub.docker.com/r/thefactory/jenkins-mesos/

FROM centos:7

MAINTAINER sheepkiller@cultdeadsheep.org

ENV MESOS_NATIVE_JAVA_LIBRARY=/usr/local/lib/libmesos.so \
    JENKINS_HOME=/home/jenkins \
    JENKINS_WARDIR=/jenkins

RUN adduser -m jenkins && \
     mkdir ${JENKINS_WARDIR} && \
     chown jenkins:jenkins ${JENKINS_WARDIR} && \
     rm -fr /home/jenkins

RUN  yum -y install /tmp/mesosphere-el-repo-7-1.noarch.rpm http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm \
        epel-release  \
        wget && \
    yum update -y && \
    yum install -y mesos \
        maven \
        sudo && \
        sed -i 's/^Defaults.*requiretty/#&/g' /etc/sudoers

ENV JAVA_MAJOR=8 \
    JAVA_UPDATE=65 \
    JAVA_BUILD=17 

RUN wget --no-cookies --no-check-certificate \
    --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    "http://download.oracle.com/otn-pub/java/jdk/${JAVA_MAJOR}u${JAVA_UPDATE}-b${JAVA_BUILD}/jdk-${JAVA_MAJOR}u${JAVA_UPDATE}-linux-x64.rpm" -O /tmp/jdk-${JAVA_MAJOR}u${JAVA_UPDATE}-linux-x64.rpm && \
     yum localinstall -y /tmp/jdk-${JAVA_MAJOR}u${JAVA_UPDATE}-linux-x64.rpm && \
    rm -f /tmp/jdk-${JAVA_MAJOR}u${JAVA_UPDATE}-linux-x64.rpm

ENV JAVA_HOME=/usr/java/jdk1.8.0_${JAVA_UPDATE} \
    JENKINS_VERSION=1.625.1 \
    MESOS_JENKINS_VERSION=0.8.0


WORKDIR ${JENKINS_WARDIR}

USER jenkins
RUN wget http://mirrors.jenkins-ci.org/war-stable/${JENKINS_VERSION}/jenkins.war && \
    wget https://github.com/jenkinsci/mesos-plugin/archive/mesos-${MESOS_JENKINS_VERSION}.tar.gz

RUN tar -xzf ${JENKINS_WARDIR}/mesos-${MESOS_JENKINS_VERSION}.tar.gz && \
    cd ${JENKINS_WARDIR}/mesos-plugin-mesos-${MESOS_JENKINS_VERSION} && \
    sed -i "s,1.565.3,${JENKINS_VERSION}," pom.xml && \
    mvn package -DskipTests -Duser.home=/tmp && \
    python -c 'import zipfile,sys; zipfile.ZipFile(sys.argv[1],"a").write(sys.argv[2],sys.argv[3])' ${JENKINS_WARDIR}/jenkins.war ${JENKINS_WARDIR}/mesos-plugin-mesos-${MESOS_JENKINS_VERSION}/target/mesos.hpi WEB-INF/plugins/mesos.hpi && \
    rm -fr ${JENKINS_WARDIR}/mesos-plugin-mesos-${MESOS_JENKINS_VERSION} ${JENKINS_WARDIR}/mesos-${MESOS_JENKINS_VERSION}.tar.gz /tmp/.m2/repository

USER root
ADD entrypoint.sh /

WORKDIR ${JENKINS_HOME}

ENTRYPOINT ["/entrypoint.sh"]
