###############################################
### Dockerfile for 10X Genomics Cell Ranger ###
###############################################

# Based on
FROM centos:8

# File Author / Maintainer
MAINTAINER Tiandao Li <litd99@gmail.com>

# Install some utilities
RUN yum install -y \
	file \
	git \
	sssd-client \
	which \
	wget \
	unzip

# Install bcl2fastq
RUN cd /tmp/ && \
	wget http://regmedsrv1.wustl.edu/Public_SPACE/litd/Public_html/pkg/bcl2fastq2-v2.20.0.422-Linux-x86_64.rpm && \
	yum -y --nogpgcheck localinstall bcl2fastq2-v2.20.0.422-Linux-x86_64.rpm && \
	rm -rf bcl2fastq2-v2.20.0.422-Linux-x86_64.rpm
 	
# Install cellranger
RUN cd /opt/ && \
	wget http://regmedsrv1.wustl.edu/Public_SPACE/litd/Public_html/pkg/cellranger-6.1.1.tar.gz && \	
	tar -xzvf cellranger-6.1.1.tar.gz && \
	rm -f cellranger-6.1.1.tar.gz

# path
ENV PATH /opt/cellranger-6.1.1:$PATH

