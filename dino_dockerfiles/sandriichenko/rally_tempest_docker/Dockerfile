FROM rallyforge/rally:0.9.0
MAINTAINER Oleksii Butenko <obutenko@mirantis.com>

WORKDIR /var/lib
USER root
RUN git clone https://git.openstack.org/openstack/tempest -b 15.0.0 && \
    pip install tempest==15.0.0 && \
    pip install ddt==1.0.1 && \
    git clone https://github.com/openstack/ironic.git && \
    git clone https://github.com/openstack/designate-tempest-plugin.git && \
    git clone https://github.com/openstack/ceilometer.git && \
    pip install -r ironic/test-requirements.txt && \
    pip install -r designate-tempest-plugin/test-requirements.txt && \
    pip install -r ceilometer/test-requirements.txt

WORKDIR /home/rally

COPY skip_lists /var/lib/skip_lists
COPY tempest_conf /var/lib/tempest_conf
COPY run_tempest.sh /usr/bin/run-tempest

ENTRYPOINT ["run-tempest"]
