FROM registry.access.redhat.com/ubi7/s2i-base
#FROM centos/s2i-base-centos7

MAINTAINER Subin Modeel<smodeel@redhat.com>

ENV BUILDER_VERSION 1.0

ARG TF_SERVING_PORT=8500
ARG TF_SERVING_REST_PORT=8501
ARG TF_SERVING_PACKAGE=https://github.com/AICoE/tensorflow-wheels/releases/download/tensorflow_serving_api-r2.1-cpu-2020-02-18_155137/tensorflow_model_server

ENV TF_SERVING_PACKAGE $TF_SERVING_PACKAGE

LABEL io.k8s.description="Tensorflow serving builder" \
      io.k8s.display-name="tensorflow serving builder" \
      io.openshift.expose-services="8500:http" \
      io.openshift.tags="tensorflow"

RUN yum install -y tree which wget \
	&& yum clean all -y \
	&& wget $TF_SERVING_PACKAGE -P /opt/app-root/ \
	&& chmod 777 /opt/app-root/tensorflow_model_server


COPY ./s2i/bin/ /usr/libexec/s2i

#Drop the root user and make the content of /opt/app-root owned by user 1001
## RUN chown -R 1001:1001 /opt/app-root

# This default user is created in the openshift/base-centos7 image
USER 1001
## COPY ./tensorflow_model_server /opt/app-root/tensorflow_model_server


EXPOSE $TF_SERVING_PORT
EXPOSE $TF_SERVING_REST_PORT

# TODO: Set the default CMD for the image
CMD ["/usr/libexec/s2i/usage"]
