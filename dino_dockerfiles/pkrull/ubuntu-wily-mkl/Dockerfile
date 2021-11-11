# Start with Ubuntu base image
FROM buildpack-deps:wily
MAINTAINER Pete Krull <pete.krull@3dsim.com>

ENV MKL_VER=l_mkl_11.3.3.210

# Install MKL dependency packages
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y \
  cpio \
  wget

# Install MKL
RUN cd /tmp && \
  wget -q http://registrationcenter-download.intel.com/akdlm/irc_nas/9068/${MKL_VER}.tgz && \
  tar xzf ${MKL_VER}.tgz && \
  cd ${MKL_VER} && \
  sed -i 's/ACCEPT_EULA=decline/ACCEPT_EULA=accept/g' silent.cfg && \
  sed -i 's/ACTIVATION_TYPE=exist_lic/ACTIVATION_TYPE=trial_lic/g' silent.cfg && \
# NOTE: Installer may complain about "Unsupported OS". Installation should still be valid.
  ./install.sh -s silent.cfg && \
# Clean up
  cd .. && rm -rf ${MKL_VER}*

# Configure dynamic link
RUN echo "/opt/intel/lib/intel64\n/opt/intel/mkl/lib/intel64" > /etc/ld.so.conf.d/mkl.conf && \
  ldconfig && \
  echo ". /opt/intel/bin/compilervars.sh intel64" >> /etc/bash.bashrc
