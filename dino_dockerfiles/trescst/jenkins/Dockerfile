FROM jenkins

MAINTAINER Steven Trescinski <steven@gluo.be>

USER root
#TODO the group ID for docker group on my Amazon Linux is 999, therefore I can only run docker commands if I have same group id inside.
# Otherwise the socket file is not accessible.
RUN groupadd -g 999 docker && usermod -a -G docker jenkins
#install libsystemd-journal0 package
RUN apt-get update && apt-get install libsystemd-journal0

USER jenkins
