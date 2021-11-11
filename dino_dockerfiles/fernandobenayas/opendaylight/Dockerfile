FROM anapsix/alpine-java:8_jdk

MAINTAINER Álvaro Carrera <a.carrera@upm.es>
#This DockerFile is based on https://hub.docker.com/r/glefevre/opendaylight/ adding feature dependencies for karaf and updating ODL version


RUN mkdir /odl
WORKDIR /odl

RUN apk add --no-cache gcc g++ make libc-dev python-dev openssl && \
    apk add maven --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/community/ && \
    wget https://nexus.opendaylight.org/content/repositories/public/org/opendaylight/integration/distribution-karaf/0.6.2-Carbon/distribution-karaf-0.6.2-Carbon.tar.gz && \
    tar -xvzf distribution-karaf-0.6.2-Carbon.tar.gz && \
    apk del gcc make python-dev libc-dev g++ maven && \
    rm -rf /var/cache/apk/*

RUN ln -s distribution-karaf-0.6.2-Carbon distribution
# 8181 : API
# 6633 : Openflow
# 8101 : ODL cli

EXPOSE 8181 6633 8101

RUN sed -i "s/featuresBoot=config,standard,region,package,kar,ssh,management/featuresBoot=config,standard,region,package,kar,ssh,management,odl-l2switch-switch-ui,odl-l2switch-all,odl-restconf,odl-mdsal-apidocs,odl-ovsdb-southbound-impl-ui,odl-dlux-core,odl-dluxapps-applications,odl-dluxapps-yangui,odl-dluxapps-yangvisualizer,odl-dluxapps-yangman,odl-dluxapps-nodes/g" /odl/distribution/etc/org.apache.karaf.features.cfg

ADD healthcheck.sh /odl/healthcheck.sh
RUN chmod +x /odl/healthcheck.sh

CMD ./distribution/bin/karaf