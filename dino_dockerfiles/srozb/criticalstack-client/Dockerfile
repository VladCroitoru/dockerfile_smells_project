FROM centos:7
MAINTAINER Slawomir Rozbicki <docker@rozbicki.eu>

RUN yum update -y \
&& curl https://packagecloud.io/install/repositories/criticalstack/critical-stack-intel/script.rpm.sh | bash \
&& yum install -y critical-stack-intel

ENTRYPOINT ["critical-stack-intel"]
CMD ["pull"]
