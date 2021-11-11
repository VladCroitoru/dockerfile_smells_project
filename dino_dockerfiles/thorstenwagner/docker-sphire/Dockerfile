# SPHIRE Installation 
# Based on CENTOS6

FROM centos:centos6

MAINTAINER Thorsten Wagner (https://github.com/thorstenwagner)

# this is a non-interactive automated build - avoid some warning messages
ENV CENTOS_FRONTEND noninteractive
RUN pwd
# update repositories
RUN yum update 

# install wget
RUN yum install wget which mesa-libGL-devel -y

# get sphire

RUN wget --no-check-certificate https://ftp.gwdg.de/pub/misc/sphire/sphire_beta_20170602/sphire_beta_20170602.linux64.centos6.sh
RUN bash sphire_beta_20170602.linux64.centos6.sh -b -p ${HOME}/SPHIRE

RUN echo "PATH=${HOME}/SPHIRE/bin:${PATH}" >> ${HOME}/.bashrc
RUN echo "PATH=${HOME}/SPHIRE/bin:${PATH}" >> ${HOME}/.bash_profile
RUN echo "PATH=${HOME}/SPHIRE/bin:${PATH}" >> ${HOME}/.profile
RUN cat ${HOME}/.bashrc
RUN source ${HOME}/.bashrc
RUN ls
RUN export PATH=${HOME}/SPHIRE/bin:${PATH}; cd ${HOME}/SPHIRE/; bash ${HOME}/SPHIRE/utils/uninstall_openmpi.sh -y
RUN export PATH=${HOME}/SPHIRE/bin:${PATH}; cd ${HOME}/SPHIRE/; bash ${HOME}/SPHIRE/utils/build_and_install_openmpi.sh 
RUN export PATH=${HOME}/SPHIRE/bin:${PATH}; cd ${HOME}/SPHIRE/; bash ${HOME}/SPHIRE/utils/build_pydusa_numpy.sh 1.8 --no-test
RUN export PATH=${HOME}/SPHIRE/bin:${PATH}; cd ${HOME}/SPHIRE/; bash ${HOME}/SPHIRE/utils/install_pydusa_numpy.sh 1.8 

# open ssh port
EXPOSE 22
