FROM ocramz/petsc-docker:latest

MAINTAINER Marco Zocca < github.com/ocramz >

# ------------------------------------------------------------
# Add an 'mpirun' user
# ------------------------------------------------------------
ENV MPIUSER=mpirun

RUN adduser --disabled-password --gecos "" ${MPIUSER} && \
    echo "${MPIUSER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

ENV MPIHOME=/home/${MPIUSER} \
    SSHDIR=${MPIHOME}/.ssh

# ------------------------------------------------------------
# Env. variables and directories
# ------------------------------------------------------------
RUN printenv | grep PETSC && \
    printenv | grep SLEPC

# # environment variables
# # NB : assumes SLEPC_ARCH is defined
ENV LOCAL_DIR=${HOME}/.local \
    BIN_DIR=${HOME}/.local/bin \
    SRC_DIR=${HOME}/src \
    PETSC_INCLUDE1=${PETSC_DIR}/include/ \
    PETSC_INCLUDE2=${PETSC_DIR}/${PETSC_ARCH}/include/ \
    PETSC_LIB=${PETSC_DIR}/${PETSC_ARCH}/lib/ \
    SLEPC_INCLUDE1=${SLEPC_DIR}/include/ \
    SLEPC_INCLUDE2=${SLEPC_DIR}/$SLEPC_ARCH/include/ \
    SLEPC_LIB=${SLEPC_DIR}/${SLEPC_ARCH}/lib/

# # # Create directories
RUN mkdir -p $LOCAL_DIR && \
    mkdir -p $BIN_DIR && \
    mkdir -p $SRC_DIR && \
    mkdir -p ${SSHDIR} && \
    mkdir -p ${MPIHOME}/bin && \
    mkdir -p ${MPIHOME}/example

# ------------------------------------------------------------
# APT-Install dependencies and tools
# ------------------------------------------------------------

RUN apt-get update && \
    apt-get -qq install -y --no-install-recommends \
          bzip2 unzip git libgmp-dev xz-utils \
 && apt-get clean && \
    apt-get purge && \
    rm -rf /var/lib/apt/lists/*


# ------------------------------------------------------------
# Get the Haskell `stack` build tool
# ------------------------------------------------------------
WORKDIR $BIN_DIR

RUN curl -L https://www.stackage.org/stack/linux-x86_64 | tar xz --wildcards --strip-components=1 -C $BIN_DIR '*/stack'

# # environment variables (derived)
ENV PATH=${BIN_DIR}:${PATH} \
    PETSCHS_DIR=${SRC_DIR}/petsc-hs
    
# RUN ls -lsA ${BIN_DIR} 

# ------------------------------------------------------------
# SHOW ENVIRONMENT VARIABLES
# ------------------------------------------------------------
RUN printenv


# ------------------------------------------------------------
# SHOW PETSC CONFIGURE OPTIONS
# ------------------------------------------------------------
RUN cat ${PETSC_DIR}/${PETSC_ARCH}/lib/petsc/conf/configure.log | grep "Configure Options"