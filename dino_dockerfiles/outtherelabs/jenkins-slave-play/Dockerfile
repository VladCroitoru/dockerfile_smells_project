# The FROM will be replaced when building in OpenShift
FROM openshift/base-centos7

# Install headless Java
USER root
RUN yum install -y --setopt=tsflags=nodocs --enablerepo=centosplus epel-release && \
    rpmkeys --import file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 && \
    export INSTALL_PKGS="java-1.8.0-openjdk-devel nss_wrapper" && \
    yum install -y --setopt=tsflags=nodocs install $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all && \
    mkdir -p /opt/app-root/jenkins && \
    chown -R 1001:0 /opt/app-root/jenkins && \
    chmod -R g+w /opt/app-root/jenkins && \
    curl -L https://github.com/openshift/origin/releases/download/v1.3.0/openshift-origin-client-tools-v1.3.0-3ab7af3d097b57f933eccef684a714f2368804e7-linux-64bit.tar.gz | \
    mv openshift*/oc /usr/local/bin && \
    rm -rf openshift-origin-client-tools-*

# Copy the entrypoint
COPY contrib/openshift/* /opt/app-root/jenkins/
USER 1001

# Pre-cache SBT
WORKDIR /opt/app-root/jenkins
ENV SBT_HOME=/opt/app-root/jenkins
ENV SBT_VERSION=0.13.12
ENV SCALA_VERSION=2.11.8
COPY barebones-app /opt/app-root/barebones
RUN cd /opt/app-root/barebones && \
    ./sbt \
      -scala-version $SCALA_VERSION \
      -sbt-version $SBT_VERSION \
      -sbt-dir $SBT_HOME/.sbt/$SBT_VERSION \
      -sbt-launch-dir $SBT_HOME/.sbt/launchers \
      -ivy $SBT_HOME/.ivy2 \
      about && \
    chown -R 1001:0 $SBT_HOME/.sbt $SBT_HOME/.ivy2 && \
    chmod -R g+w $SBT_HOME/.sbt $SBT_HOME/.ivy2

# Run the JNLP client by default
# To use swarm client, specify "/opt/app-root/jenkins/run-swarm-client" as Command
ENTRYPOINT ["/opt/app-root/jenkins/run-jnlp-client"]
