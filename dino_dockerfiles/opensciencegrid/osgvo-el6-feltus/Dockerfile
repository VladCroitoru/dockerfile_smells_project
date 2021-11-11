FROM opensciencegrid/osgvo-el6

RUN yum -y upgrade

RUN rpm --import https://packages.irods.org/irods-signing-key.asc && \
    wget -q -O /etc/yum.repos.d/renci-irods.yum.repo https://packages.irods.org/renci-irods.yum.repo && \
    yum -y update && \
    yum -y install irods-icommands

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

