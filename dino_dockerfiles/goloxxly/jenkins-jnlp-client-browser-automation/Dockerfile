FROM goloxxly/jenkins-jnlp-client-gradle:3.1.0

LABEL maintainer "gyorgy.novak@openplus.co.uk"

RUN yum install -y Xvfb firefox \
    && yum -y clean all

ADD run.sh /
RUN chmod +x /run.sh

ENV DISPLAY :10

ENTRYPOINT ["/run.sh"]
