FROM centos/python-27-centos7
MAINTAINER Isaac Kwan <isaackwan@link.cuhk.edu.hk>

USER root

RUN yum -y install ImageMagick && yum clean all
COPY policy.xml /etc/ImageMagick/policy.xml

USER 1001
