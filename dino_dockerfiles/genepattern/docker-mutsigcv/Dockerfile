# copyright 2017-2018 Regents of the University of California and the Broad Institute. All rights reserved.
FROM ubuntu:14.04

RUN \
     apt-get update \
  && apt-get install -y \
    wget \
    curl \
    zip \
    unzip \
    xorg \
  && rm -rf /var/lib/apt/lists/*

# Install Matlab Component Runtime
#   <run-with-env> -u Matlab-2013a-MCR 
#   MATLAB Release: R2013a (8.1)
#   MATLAB Component Runtime (MCR): 8.1

ENV MCR_BASE="/opt/matlab-mcr"
ENV MCR_VERSION="v81"
ENV MCR_HOME="${MCR_BASE}/${MCR_VERSION}"

RUN mkdir -p ${MCR_BASE} \
  && mcr_install_dir=${mcr_base}_install \
  && mkdir -p ${mcr_install_dir} \
  && cd ${mcr_install_dir} \
  && wget http://ssd.mathworks.com/supportfiles/MCR_Runtime/R2013a/MCR_R2013a_glnxa64_installer.zip \
  && unzip -q MCR_R2013a_glnxa64_installer.zip \
  && ./install -mode silent -agreeToLicense yes -destinationFolder ${MCR_BASE} \
  && cd / \
  && rm -rf ${mcr_install_dir}

ENV LD_LIBRARY_PATH="${MCR_HOME}/runtime/glnxa64:${MCR_HOME}/bin/glnxa64:${MCR_HOME}/sys/os/glnxa64:${MCR_HOME}/sys/java/jre/glnxa64/jre/lib/amd64/native_threads:${MCR_HOME}/sys/java/jre/glnxa64/jre/lib/amd64/server:${MCR_HOME}/sys/java/jre/glnxa64/jre/lib/amd64"
ENV XAPPLRESDIR="${MCR_HOME}/X11/app-defaults"

#
# Install MutSigCV binary
#
ENV MUTSIG_HOME /opt/mutsig
RUN mkdir -p ${MUTSIG_HOME}/bin
COPY gp_MutSigCV ${MUTSIG_HOME}/bin
RUN chmod u+x ${MUTSIG_HOME}/bin/gp_MutSigCV
COPY gp_MutSigCV.ctf ${MUTSIG_HOME}/bin
ENV PATH=${MUTSIG_HOME}/bin:${PATH}

CMD ["gp_MutSigCV"]
