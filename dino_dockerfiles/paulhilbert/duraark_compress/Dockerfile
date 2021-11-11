FROM paulhilbert/wp4_wp5_stripped_base:latest
MAINTAINER Richard Vock <vock@cs.uni-bonn.de>
ADD docker_build.sh /tmp/build.sh
ADD docker_build_all.sh /tmp/build_all.sh
RUN /bin/sh /tmp/build_all.sh
#ENTRYPOINT ["diffdetect"]
