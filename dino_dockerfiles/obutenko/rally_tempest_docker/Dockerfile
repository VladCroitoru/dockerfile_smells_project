FROM xrally/xrally-openstack:0.9.1
MAINTAINER Oleksii Butenko <obutenko@mirantis.com>

WORKDIR /var/lib
USER root
RUN git clone https://git.openstack.org/openstack/tempest -b 16.0.0 && \
    pip install tempest==16.0.0 && \
    pip install ansible==2.3 && \
    pip install ddt==1.0.1
    
WORKDIR /home/rally

COPY tmp.conf /var/lib/tmp.conf
COPY run_tempest.sh /usr/bin/run-tempest

ENTRYPOINT ["run-tempest"]
