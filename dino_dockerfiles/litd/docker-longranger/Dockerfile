###############################################
### Dockerfile for 10X Genomics Long Ranger ###
###############################################

# Based on
FROM centos:7

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
	wget https://support.illumina.com/content/dam/illumina-support/documents/downloads/software/bcl2fastq/bcl2fastq2-v2-19-1-linux.zip && \
	unzip bcl2fastq2-v2-19-1-linux.zip && \
	yum -y --nogpgcheck localinstall bcl2fastq2-v2.19.1.403-Linux-x86_64.rpm && \
	rm -rf bcl2fastq2-v2-19-1-linux.zip
 	
# Install cellranger
RUN cd /tmp/ && \
	wget -O longranger-2.1.5.tar.gz "http://cf.10xgenomics.com/releases/genome/longranger-2.1.5.tar.gz?Expires=1501730695&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cDovL2NmLjEweGdlbm9taWNzLmNvbS9yZWxlYXNlcy9nZW5vbWUvbG9uZ3Jhbmdlci0yLjEuNS50YXIuZ3oiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE1MDE3MzA2OTV9fX1dfQ__&Signature=G0tW5M5gkkCSTh6HL5DLe6MME9G7~hONUVombhbLumQ6zVhDmuRAOSTaI61OSledCP5jwar5mzFpODhK5FKoQXYbiy-yA6Ag9dQHTR1uk8~ewv9KuwZVOSBgsrqoeK7coML2NUptO2yhybgTh7em7keBJ4Pt4i11Zh6z9YdUrv6a2F851DNYaL2Lr9sXuUEpBLvO~hcKDDmaPbqGdUE6eqEkGAEzcbEHRj7rgcHewJGt6IMNAzP~z~OS76cxG7KWPK3Atbx47Kd8KTgVnguWqlNmw0aAMEqGuo3W3fN-NFno6wicZFAv7RnN5wgAHGEjfEz1ilissSF2SVKuDm7z-g__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA" && \
	mv longranger-2.1.5.tar.gz /opt/ && \
	cd /opt/ && \
	tar -xzvf longranger-2.1.5.tar.gz && \
	rm -f longranger-2.1.5.tar.gz

# path
ENV PATH /opt/longranger-2.1.5:$PATH

