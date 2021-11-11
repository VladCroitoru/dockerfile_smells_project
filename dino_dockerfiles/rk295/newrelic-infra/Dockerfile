FROM centos:7

MAINTAINER Robin Kearney <robin@kearney.co.uk>

RUN curl -o /etc/yum.repos.d/newrelic-infra.repo https://download.newrelic.com/infrastructure_agent/linux/yum/el/7/x86_64/newrelic-infra.repo

RUN yum --nogpgcheck makecache fast && \
    yum -y --nogpgcheck install newrelic-infra dmidecode policycoreutils && \
    yum clean all

ADD newrelic-infra.yml /etc/

# Set log level to a sane default
ENV NRIA_LOGLEVEL="info"
ENV NRIA_VERBOSE=0

# This assumes you mount the host ROOT directory read-only
# inside the container at /mnt/ROOT eg: -v /:/mnt/ROOT:ro
ENV NRIA_OVERRIDE_HOST_ROOT="/mnt/ROOT"

# Really you ought to pass this at deployment time.
ENV NRIA_LICENSE_KEY="null"

CMD ["/usr/bin/newrelic-infra","-config","/etc/newrelic-infra.yml"]

# LABELs commented out for now, maybe investigate swarm and ECS labels too
# LABEL io.k8s.description="New Relic Linux Infrastructure Agent" \
#       io.k8s.display-name="newrelic-infra"
