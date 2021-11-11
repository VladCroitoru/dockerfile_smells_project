FROM centos:7

# Set one or more individual labels
LABEL dockeruser="intendo"
LABEL maintainer="Darren.Curtis@pnnl.gov"
LABEL description="A minimal CentOS image for sofware development"
LABEL vendor="Pacific Northwest National Laboratory"
LABEL package_name="centos7"
LABEL version="1.1.0"
LABEL release-date="2017-07-26"
LABEL version.is-production="yes"


# ##########################################################
#   CENTOS 7 Development Environment
# ##########################################################
RUN yum -y groupinstall 'Development Tools'             && \
    yum -y install autotools                               \
                   iproute                                 \
                   libpcap-devel                           \
                   libpcap                                 \
                   wget                                    \
                   which                                && \
    yum -y clean all

# ##########################################################
#   SYSTEM set time to UTC
# ##########################################################
ENV TZ=UTC
RUN /bin/rm -f /etc/localtime                           && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime

ENTRYPOINT ["/bin/bash"]
