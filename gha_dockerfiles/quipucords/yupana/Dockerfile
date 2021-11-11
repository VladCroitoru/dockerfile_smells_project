# yupana-ubi7
FROM registry.access.redhat.com/ubi7/python-36:latest

EXPOSE 8080

ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    PIP_NO_CACHE_DIR=off \
    ENABLE_PIPENV=true \
    APP_HOME="/opt/app-root/src/yupana" \
    APP_MODULE="config.wsgi"

ENV SUMMARY="Yupana is a subscriptions services application" \
    DESCRIPTION="Yupana is a subscriptions services application"

LABEL summary="$SUMMARY" \
    description="$DESCRIPTION" \
    io.k8s.description="$DESCRIPTION" \
    io.k8s.display-name="Yupana" \
    io.openshift.expose-services="8080:http" \
    io.openshift.tags="builder,python,python36,rh-python36" \
    com.redhat.component="python36-docker" \
    name="Yupana" \
    version="1" \
    maintainer="Red Hat Subscription Management Services"

USER root

RUN INSTALL_PKGS="rh-python36 rh-python36-python-devel rh-python36-python-setuptools rh-python36-python-pip nss_wrapper \
    httpd24 httpd24-httpd-devel httpd24-mod_ssl httpd24-mod_auth_kerb httpd24-mod_ldap \
    httpd24-mod_session atlas-devel gcc-gfortran libffi-devel libtool-ltdl enchant \
    " && \
    yum install -y yum-utils && \
    prepare-yum-repositories rhel-server-rhscl-7-rpms && \
    yum -y --setopt=tsflags=nodocs install $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum -y clean all --enablerepo='*'

# sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./openshift/s2i/bin/ $STI_SCRIPTS_PATH

# if we have any extra files we should copy them over
COPY openshift/root /

# Copy application files to the image.
COPY . ${APP_ROOT}/src

# - Create a Python virtual environment for use by any application to avoid
#   potential conflicts with Python packages preinstalled in the main Python
#   installation.
# - In order to drop the root user, we have to make some directories world
#   writable as OpenShift default security model is to run the container
#   under random UID.
RUN source scl_source enable rh-python36 && \
    virtualenv ${APP_ROOT} && \
    chown -R 1001:0 ${APP_ROOT} && \
    fix-permissions ${APP_ROOT} -P && \
    rpm-file-permissions && \
    $STI_SCRIPTS_PATH/assemble

USER 1001

# Set the default CMD
CMD $STI_SCRIPTS_PATH/run
