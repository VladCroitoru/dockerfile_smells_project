FROM utestfactory/centos_compile_utest:6
MAINTAINER The U-TEST Team

ENV JENKINS_PUBLIC_KEY="define" \
    GITLAB_SSH_PRIVATE_KEY="define"

RUN yum install -y openssh-server
RUN useradd -ms /bin/bash jenkins
# Set password for the jenkins user (you may want to alter this).
RUN echo -e "jenkins:jenkins\nroot:gc" | chpasswd

# Standard SSH port
EXPOSE 22

COPY run.sh /run.sh

ENTRYPOINT ["/run.sh"]
