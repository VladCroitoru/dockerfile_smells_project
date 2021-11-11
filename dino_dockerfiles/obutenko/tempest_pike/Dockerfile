FROM xrally/xrally-openstack:0.10.1
MAINTAINER Oleksii Butenko <apbutenko@gmail.com>

WORKDIR /var/lib
USER root
RUN git clone https://git.openstack.org/openstack/tempest -b 17.2.0 && \
    pip install tempest==17.2.0
    
WORKDIR /home/rally

COPY tempest.conf /var/lib/tempest.conf
COPY run-tempest.sh /usr/bin/run-tempest

ENTRYPOINT ["run-tempest"]
