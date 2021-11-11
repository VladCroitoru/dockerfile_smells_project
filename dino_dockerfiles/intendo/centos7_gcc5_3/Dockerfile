FROM intendo/centos7

# Set one or more individual labels
LABEL dockeruser="intendo"
LABEL maintainer="Darren.Curtis@pnnl.gov"
LABEL description="CentOS image for GNU GCC/G++ sofware development"
LABEL vendor="Pacific Northwest National Laboratory"
LABEL package_name="centos7_gcc"
LABEL version="1.1.0"
LABEL release-date="2017-07-21"
LABEL version.is-production="yes"


# ##########################################################
#   GNU g++ 5.3.0 Development Environment
# ##########################################################
COPY gcc-build.sh /usr/local/gcc-build.sh
WORKDIR /usr/local
RUN /usr/local/gcc-build.sh

ENTRYPOINT ["/bin/bash"]
