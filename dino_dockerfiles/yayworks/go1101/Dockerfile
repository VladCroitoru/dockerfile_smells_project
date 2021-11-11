FROM nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04
LABEL maintainer="Nimbix, Inc."

# Update SERIAL_NUMBER to force rebuild of all layers (don't use cached layers)
ARG SERIAL_NUMBER
ENV SERIAL_NUMBER ${SERIAL_NUMBER:-20180729.1545}

ARG GIT_BRANCH
ENV GIT_BRANCH ${GIT_BRANCH:-master}

RUN apt-get -y update && \
    apt-get -y install curl && \
    curl -H 'Cache-Control: no-cache' \
        https://raw.githubusercontent.com/nimbix/image-common/master/install-nimbix.sh \
        | bash -s -- --setup-nimbix-desktop --image-common-branch $GIT_BRANCH

# Install CUDA samples
RUN apt-get -y install cuda-samples-9-1 && apt-get clean

# Fix VirtualGL for sudo
RUN chmod u+s /usr/lib/libdlfaker.so /usr/lib/libvglfaker.so

# Metadata
COPY NAE/AppDef.json /etc/NAE/AppDef.json
RUN curl --fail -X POST -d @/etc/NAE/AppDef.json https://api.jarvice.com/jarvice/validate

# Install requirements (gcc & g++)
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common python-software-properties \
    build-essential \
    awscli \
    expect \
    curl \
    git \
    make \
    tcl \
    wget \
    libibverbs-dev \
    libibverbs1 \
    librdmacm1 \
    librdmacm-dev \
    rdmacm-utils \
    libibmad-dev \
    libibmad5 \
    byacc \
    libibumad-dev \
    libibumad3 \
    flex \
    gfortran && \
    apt-get install -y python3.4 && \
    apt-get install -y python3-pip && \
    apt-get install -y python-qt4 && \ 
    apt-get install -y nodejs-legacy && \
    apt-get install -y npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install PGI
#ENV PGI_VERSION 18.4
#ENV PGI_INSTALL_DIR /opt/pgi
#ENV PGI_HOME    ${PGI_INSTALL_DIR}/linux86-64/${PGI_VERSION}
#ENV PGI_BIN_DIR ${PGI_HOME}/bin
#ENV PGI_LIB_DIR ${PGI_HOME}/lib
#ENV PGI_MAN_DIR ${PGI_HOME}/man
#ENV PGI_MPI_BIN ${PGI_HOME}/mpi/openmpi/bin
#ENV PGI_MPI_LIB ${PGI_HOME}/mpi/openmpi/lib
#ENV PGI_MPI_MAN ${PGI_HOME}/mpi/openmpi/man

#RUN wget -O/tmp/pgilinux-2018-184-x86-64.tar.gz https://s3.amazonaws.com/gen-purpose/pgilinux-2018-184-x86-64.tar.gz && \
#    cd /tmp && \
#    tar xvfz pgilinux-2018-184-x86-64.tar.gz 

#RUN export PGI_SILENT=true && \
#    export PGI_ACCEPT_EULA=accept && \
#    export PGI_INSTALL_NVIDIA=true && \
#    export PGI_INSTALL_MANAGED=true && \
#    export PGI_INSTALL_AMD=false && \
#    export PGI_INSTALL_JAVA=false && \
#    export PGI_INSTALL_MPI=true && \
#    export PGI_MPI_GPU_SUPPORT=true && \
#    /tmp/install && \
#    rm -rf /tmp/*

#RUN echo "${PGI_LIB_DIR}" >> /etc/ld.so.conf.d/pgi.conf

#ENV PATH            ${PGI_BIN_DIR}:${PGI_MPI_BIN}:${PATH}
#ENV LD_LIBRARY_PATH ${PGI_LIB_DIR}:${PGI_MPI_LIB}:${LD_LIBRARY_PATH}
#ENV MANPATH         ${PGI_MAN_DIR}:${PGI_MPI_MAN}:${MANPATH}

# nvidia-docker 1.0
LABEL com.nvidia.volumes.needed="nvidia_driver"

RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH            /usr/local/nvidia/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}

# nvidia-docker 2.0
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

## Install YayBench stuff
RUN wget -O- -q http://s3tools.org/repo/deb-all/stable/s3tools.key | apt-key add - 
RUN wget -O/etc/apt/sources.list.d/s3tools.list http://s3tools.org/repo/deb-all/stable/s3tools.list 
RUN apt-get update 
RUN apt-get install -y s3cmd 

ENV MPI_VERSION 3.1.1
RUN wget https://www.open-mpi.org/software/ompi/v3.1/downloads/openmpi-${MPI_VERSION}.tar.bz2 && \
    tar xvf openmpi-${MPI_VERSION}.tar.bz2 && \
    cd openmpi-${MPI_VERSION} && \
    ./configure --with-cuda=/usr/local/cuda  --enable-mpi-cxx --prefix=/usr/local/openmpi-${MPI_VERSION} && \
    make -j4 && \
    make install

#ENV OSU_VERSION 5.3.2
#ADD ./install-osu.sh /tmp/install-osu.sh
#RUN /bin/bash -x /tmp/install-osu.sh && rm -rf /tmp/install-osu.sh

ADD ./yb-sw-config.NIMBIX.x8664.turbotensor.sh /tmp/yb-sw-config.NIMBIX.x8664.turbotensor.sh
RUN /bin/bash -x /tmp/yb-sw-config.NIMBIX.x8664.turbotensor.sh 

WORKDIR /home/nimbix
RUN /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/admin/yb-admin.NIMBIX.x86_64.tar && \
    tar xvf yb-admin.NIMBIX.x86_64.tar -C /usr/bin 

ADD ./jupyterhub_config.py /usr/local
ADD ./wetty.tar.gz /usr/local
ADD ./config.sh /usr/local/config.sh
ADD ./start.sh /usr/local/start.sh
ADD ./setup.x /usr/local/setup.x
ADD ./jpy_lab_start.sh /usr/local/jpy_lab_start.sh
RUN chmod +x /usr/local/config.sh && chown nimbix.nimbix /usr/local/config.sh && \
    chmod +x /usr/local/start.sh && chown nimbix.nimbix /usr/local/start.sh && \
    chmod +x /usr/local/setup.x && chown nimbix.nimbix /usr/local/setup.x && \
    chmod +x /usr/local/jpy_lab_start.sh 
 
    
RUN sudo apt-get install -y r-base && \
    sudo apt-get install -y r-base-dev && \
    sudo apt-get install -y gdebi-core 
RUN /usr/bin/wget https://download2.rstudio.org/rstudio-server-1.1.442-amd64.deb && \
    echo "y" |sudo gdebi rstudio-server-1.1.442-amd64.deb && \
    echo "auth-minimum-user-id=500" >> /etc/rstudio/rserver.conf && \
    echo "Y" | /usr/local/anaconda3/bin/conda install -c r r-irkernel && \
    rm rstudio-server-1.1.442-amd64.deb 

RUN echo " " | sudo apt-add-repository ppa:octave/stable && \
    sudo apt-get update && \
    sudo apt-get install -y octave && \
    sudo apt-get build-dep -y octave && \
    echo "Y" | /usr/local/anaconda3/bin/conda install -c conda-forge octave_kernel
    
RUN sudo apt-get update && \
    sudo apt-get install -y scilab && \
#    sudo ln -s /usr/local/anaconda3/bin/pip /usr/bin/pip && \
    sudo /usr/local/anaconda3/bin/pip install msgpack && \
    sudo /usr/local/anaconda3/bin/pip install scilab_kernel
    
RUN sudo /usr/local/anaconda3/bin/pip install jupyter_c_kernel && \
    sudo /usr/local/anaconda3/bin/install_c_kernel


RUN mkdir -p /opt/images && \
    mkdir -p /opt/icons

ADD ./scripts /usr/local/scripts

# Add PushToCompute Work Flow Metadata
ADD ./NAE/nvidia.cfg /etc/NAE/nvidia.cfg
# Metadata
#COPY NAE/AppDef.json /etc/NAE/AppDef.json
#RUN curl --fail -X POST -d @/etc/NAE/AppDef.json https://api.jarvice.com/jarvice/validate

ADD ./NAE/screenshot.png /etc/NAE/screenshot.png
ADD ./Wallpaper-yaybench_1280x720.png /opt/images/Wallpaper.png
ADD ./yaymark_57x57.png /opt/icons/yaybench.png
ADD ./xfce4-desktop.xml /etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
ADD ./xfce4-panel.xml /etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml

CMD /usr/local/scripts/start.sh
CMD /usr/local/scripts/update_drivers.sh

#ADD ./install_comp.sh  /usr/local/install_comp.sh
#ADD ./expect.sh        /usr/local/expect.sh
#RUN  chmod +x          /usr/local/install_comp.sh
#RUN  chmod +x          /usr/local/expect.sh
#RUN /bin/bash -x       /usr/local/install_comp.sh
ADD ./install_cmake.sh /usr/local/install_cmake.sh
RUN  chmod +x          /usr/local/install_cmake.sh
RUN /bin/bash -x       /usr/local/install_cmake.sh
#Add AMD AOCC Compilers

#WORKDIR /usr/local
#RUN sudo wget https://s3.amazonaws.com/gen-purpose/AOCC-1.2-Fortran-Prerequisites.tar.xz && \
#    sudo wget https://s3.amazonaws.com/gen-purpose/AOCC-1.2-FortranPlugin.tar.xz && \
#    sudo wget https://s3.amazonaws.com/gen-purpose/AOCC-1.2-Compiler.tar.xz && \
#    sudo tar xf AOCC-1.2-Compiler.tar.xz && \
#    sudo wget https://s3.amazonaws.com/gen-purpose/AMDuProf_Linux_x64_1.2.275.tar.gz && \
#    sudo tar xvfz AMDuProf_Linux_x64_1.2.275.tar.gz && \
#    sudo wget https://s3.amazonaws.com/gen-purpose/AMD-LIBM-Linux-3.2.1.tar.gz && \
#    sudo tar xvfz AMD-LIBM-Linux-3.2.1.tar.gz && \
#    sudo wget https://s3.amazonaws.com/gen-purpose/AMD-BLIS-Linux-0.95-Beta.tar.gz && \
#    sudo tar xvfz AMD-BLIS-Linux-0.95-Beta.tar.gz && \
#    sudo rm -rf /usr/local/*tar* && \
#    cd AOCC-1.2-Compiler && \
#    sudo ./install.sh && \
#    sudo ln -s /usr/local/AOCC-1.2-Compiler/AOCC-1.2-FortranPlugin/dragonegg.so /usr/lib/dragonegg.so && \
#    sudo ln -s /usr/local/amdlibm-3.2.1/lib/dynamic/libamdlibm.so /usr/lib/libamdlibm.so && \
#    sudo ln -s /usr/local/amd-blis-0.95-beta/lib/libblis.so /usr/lib/libblis.so && \
#    sudo cp -r /usr/local/amd-blis-0.95-beta/include/blis /usr/include 

RUN echo 'export PATH=/usr/local/cuda/bin:/usr/local/anaconda3/envs/tensorflow/bin:${PATH}' >> /home/nimbix/.bashrc \
&&  echo 'export PYTHONPATH=/usr/local/anaconda3/envs/tensorflow/lib/python3.6:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-packages/:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-packages/prettytensor-0.7.2-py3.6.egg:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-packages/enum34-1.1.6-py3.6.egg:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-packages/matplotlib:${PYTHONPATH}' >> /home/nimbix/.bashrc \
&&  echo 'export PATH=/usr/local/cuda/bin:/usr/local/anaconda3/envs/tensorflow/bin:$PATH' >> /etc/skel/.bashrc \
&&  echo 'export PATH=/opt/cmake/bin:$PATH' >> /etc/skel/.bashrc \
#&&  echo 'export PATH=$PATH:/opt/pgi/linux86-64/18.4/bin' >> /etc/skel/.bashrc \
#&&  echo 'export PATH=$PATH:/opt/pgi/linux86-64/18.4/lib' >> /etc/skel/.bashrc \
#&&  echo 'export PATH=$PATH:/opt/pgi/linux86-64/18.4/man' >> /etc/skel/.bashrc \
#&&  echo 'export PATH=$PATH:/opt/pgi/linux86-64/18.4/mpi/openmpi/bin' >> /etc/skel/.bashrc \
#&&  echo 'export PATH=$PATH:/opt/pgi/linux86-64/18.4/mpi/openmpi/lib' >> /etc/skel/.bashrc \
#&&  echo 'export PATH=$PATH:/opt/pgi/linux86-64/18.4/mpi/openmpi/man' >> /etc/skel/.bashrc \
&&  echo 'export PATH=/usr/local/openmpi-3.1.1/bin:$PATH' >> /etc/skel/.bashrc \
&&  echo 'export LD_LIBRARY_PATH=/usr/local/openmpi-3.1.1/lib:$LD_LIBRARY_PATH' >> /etc/skel/.bashrc \
#&&  echo 'export PATH=$PATH:/usr/local/AMDuProf_Linux_x64_1.2.275/bin' >> /etc/skel/.bashrc \
#&&  echo 'export PATH=$PATH:/usr/local/AOCC-1.2-Compiler/bin' >> /etc/skel/.bashrc \
#&&  echo 'source /usr/local/setenv_AOCC.sh' >> /etc/skel/.bashrc \
&&  echo 'export PYTHONPATH=/usr/local/anaconda3/envs/tensorflow/lib/python3.6:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-packages/:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-packages/prettytensor-0.7.2-py3.6.egg:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-packages/enum34-1.1.6-py3.6.egg:/usr/local/anaconda3/envs/tensorflow/lib/python3.6/site-packages/matplotlib:$PYTHONPATH' >> /etc/skel/.bashrc
   

# Expose port 22 for local JARVICE emulation in docker
EXPOSE 22

# for standalone use
EXPOSE 5901
EXPOSE 443




