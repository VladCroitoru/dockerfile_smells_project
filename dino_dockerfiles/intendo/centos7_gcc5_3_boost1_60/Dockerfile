FROM intendo/centos7_gcc5_3

# Set one or more individual labels
LABEL dockeruser="intendo"
LABEL maintainer="Darren.Curtis@pnnl.gov"
LABEL description="CentOS image for GNU GCC/G++ sofware development"
LABEL vendor="Pacific Northwest National Laboratory"
LABEL package_name="centos7_gcc_boost"
LABEL version="1.1.0"
LABEL release-date="2017-07-21"
LABEL version.is-production="yes"


# ##########################################################
#   BOOST 1.60.0 Development Environment
# ##########################################################
COPY boost-build.sh /usr/local/boost-build.sh
WORKDIR /usr/local
RUN /usr/local/boost-build.sh


ENTRYPOINT ["/bin/bash"]
