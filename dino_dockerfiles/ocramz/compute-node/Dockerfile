# # compute-node : a generic compute node image using Slurm and Munge

# # `docker-phusion-supervisor` contains:
# # * supervisord
# # * consul-template

# # `compute-master-node` inherits from `docker-phusion-supervisor` and adds:
# # * munge, libmunge2, libmunge-dev
# # * slurm-llnl

FROM ocramz/compute-master-node

ENV USER mpirun

# ------------------------------------------------------------
# user 'mpirun' was created in compute-master-node
# ------------------------------------------------------------


ENV HOME /home/${USER}

# # # environment variables misc.
ENV BIN_DIR=${HOME}/bin \
    SRC_DIR=${HOME}/src \
    TMP=${HOME}/tmp \
    SSHDIR=${HOME}/.ssh \
    ETC=${HOME}/etc

# # augment PATH
ENV PATH $BIN_DIR:$PATH

# # # Create directories
RUN mkdir -p $BIN_DIR && \
    mkdir -p $SRC_DIR && \
    mkdir -p $TMP && \
    mkdir -p $ETC && \
    mkdir -p $SSHDIR && \
    mkdir -p $HOME/bin



# # update TLS-related stuff and install tools
RUN apt-get update && \
    apt-get -qq install -y --no-install-recommends ca-certificates debian-keyring debian-archive-keyring && \
    apt-key update && \
    apt-get -qq update && \
    apt-get -qq install -y --no-install-recommends gcc gfortran python pkg-config perl && \
    apt-get clean
						   



# # check env
RUN printenv | grep DIR
RUN ls -lsA $HOME
# # where is the kernel ? 
RUN cat /proc/cmdline


# # # == BLCR dependencies
# RUN find ~ -name version.h
# RUN find ~ -name vmlinux








# # # ==== BLCR (checkpoint/restart for MPI libraries)

# ENV BLCR_VER 0.8.5

# # # from source 
# RUN wget http://crd.lbl.gov/assets/Uploads/FTG/Projects/CheckpointRestart/downloads/blcr-$BLCR_VER.tar.gz && tar zxf blcr-$BLCR_VER.tar.gz && cd blcr-$BLCR_VER && mkdir builddir && cd builddir && ../configure --with-linux=$KERNEL_PATH && make && make install && make insmod check

# # # => NB!!! : BLCR kernel modules should be loaded with `insmod` for BLCR to work, see https://upc-bugs.lbl.gov/blcr/doc/html/BLCR_Admin_Guide.html









# # # ==== MUNGE

# # # add MUNGE RSA key
# ADD munge.key /etc/munge/





# # # ==== SLURM







# # # test MUNGE

# # RUN /usr/sbin/munged

# # RUN munge -n | unmunge

# RUN remunge






# # # configuration

ADD etc/supervisor.d/slurmd.ini /etc/supervisor.d/

ADD etc/consul.d/slurmd.json /etc/consul.d/


# # # slurmd health check scripts

ADD /opt/slurm/bin/check_slurmd.sh /opt/slurm/bin/
ADD /opt/slurm/bin/restart.sh /opt/slurm/bin/



# # # === expose TCP/IP ports

EXPOSE 22
# 2376 for TLS
EXPOSE 2375


WORKDIR $HOME

# # # clean local package archive
RUN apt-get clean