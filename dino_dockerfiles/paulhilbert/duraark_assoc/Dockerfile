FROM paulhilbert/wp4_wp5_stripped_base:latest
MAINTAINER Richard Vock <vock@cs.uni-bonn.de>
ADD docker_build.sh /tmp/build.sh
RUN /bin/sh /tmp/build.sh duraark_assoc
ENTRYPOINT ["compute_associations"]
