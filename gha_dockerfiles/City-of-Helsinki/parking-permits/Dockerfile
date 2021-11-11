# Dockerfile for Parking Permits backend

# ==============================
FROM registry.access.redhat.com/ubi8/python-39 as appbase
# ==============================

USER root

RUN rm /etc/rhsm-host

ARG LOCAL_REDHAT_USERNAME
ARG LOCAL_REDHAT_PASSWORD
ARG BUILD_MODE

RUN if [ "x$BUILD_MODE" = "xlocal" ] ;\
    then \
        subscription-manager register --username $LOCAL_REDHAT_USERNAME --password $LOCAL_REDHAT_PASSWORD --auto-attach; \
    else \
        subscription-manager register --username ${REDHAT_USERNAME} --password ${REDHAT_PASSWORD} --auto-attach; \
    fi

RUN subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms
RUN yum -y update

RUN rpm -Uvh https://download.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

RUN yum install -y gdal

RUN useradd -ms /bin/bash -d /app parking_permits

RUN chown parking_permits /opt/app-root/lib/python3.9/site-packages
RUN chown parking_permits /opt/app-root/lib/python3.9/site-packages/*

WORKDIR /app

RUN subscription-manager remove --all

# Add tini init system https://github.com/krallin/tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

ENV PYTHONDONTWRITEBYTECODE True
ENV PYTHONUNBUFFERED True

# Copy and install requirements files to image
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY docker-entrypoint.sh /app/
ENTRYPOINT ["/tini", "--", "/app/docker-entrypoint.sh"]

EXPOSE 8888

# ==============================
FROM appbase as development_stage
# ==============================

# git is needed for 'pre-commit install' to work
RUN yum install git

COPY requirements-dev.txt /app/
RUN pip install --no-cache-dir -r /app/requirements-dev.txt

COPY requirements-test.txt /app/
RUN pip install --no-cache-dir -r /app/requirements-test.txt

COPY . /app/

RUN chgrp -R 0 /app
RUN chmod g=u -R /app

# ==============================
FROM appbase as production_stage
# ==============================

COPY . /app/

RUN chgrp -R 0 /app
RUN chmod g=u -R /app

RUN DJANGO_SECRET_KEY="only-used-for-collectstatic" DATABASE_URL="sqlite:///" \
    python /app/manage.py collectstatic --noinput
