# playbook2image
FROM openshift/base-centos7

MAINTAINER Aaron Weitekamp <aweiteka@redhat.com>

# TODO: Rename the builder environment variable to inform users about application you provide them
# ENV BUILDER_VERSION 1.0

LABEL io.k8s.description="Ansible playbook to image builder" \
      io.k8s.display-name="playbook2image" \
      io.openshift.tags="builder,ansible,playbook" \
      url="https://github.com/aweiteka/playbook2image/blob/master/README.md" \
      name="playbook2image" \
      summary="Ansible playbook to image builder" \
      description="Base image to to ship Ansible playbooks as self-executing container image." \
      vcs-url="https://github.com/aweiteka/playbook2image" \
      vcs-type="git" \
      version="alpha"

# ansible and pip are in EPEL
RUN yum install -y epel-release && yum clean all -y

# workaround for https://github.com/openshift/openshift-ansible/issues/3111
# install ansible via pip to lock version
#RUN yum install -y  --setopt=tsflags=nodocs ansible python-pip python-devel && yum clean all -y
RUN yum install -y  --setopt=tsflags=nodocs python-pip python-devel && yum clean all -y
RUN pip install -Iv ansible==2.2.0.0

# TODO (optional): Copy the builder files into /opt/app-root
#COPY ./<builder_folder>/ /opt/app-root/

# TODO: Copy the S2I scripts to /usr/libexec/s2i, since openshift/base-centos7 image sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./.s2i/bin/ /usr/libexec/s2i
COPY user_setup /tmp
ADD README.md /help.1

ENV APP_ROOT=/opt/app-root
ENV USER_NAME=default \
    USER_UID=1001 \
    APP_HOME=${APP_ROOT}/src \
    PATH=$PATH:${APP_ROOT}/bin
RUN mkdir -p ${APP_HOME} ${APP_ROOT}/etc ${APP_ROOT}/bin
RUN chmod -R ug+x ${APP_ROOT}/bin ${APP_ROOT}/etc /tmp/user_setup && \
    /tmp/user_setup

# This default user is created in the openshift/base-centos7 image
USER ${USER_UID}

RUN sed "s@${USER_NAME}:x:${USER_UID}:0@${USER_NAME}:x:\${USER_ID}:\${GROUP_ID}@g" /etc/passwd > ${APP_ROOT}/etc/passwd.template
CMD ["/usr/libexec/s2i/usage"]
