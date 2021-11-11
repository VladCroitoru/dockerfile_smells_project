FROM twobombs/deploy-nvidia-docker

# force yes, force install 
COPY 90forceyes /etc/apt/apt.conf.d/

# add cl dev apps & dependancies
RUN apt-get update && apt-get install -y git software-properties-common ant freeglut3-dev openjdk-8-jdk qv4l2 ocl-icd-opencl-dev oclgrind python-setuptools python3-setuptools dkms && apt-get clean all && apt -y autoremove

# add CL drivers
# Aspeed onboard
# RUN cd /root && wget -q http://upload.aspeedtech.com/BIOS/v103_linux_freebsd_solaris.zip && unzip /root/v103_linux_freebsd_solaris.zip && rm *.zip
# Intel
# old: RUN cd /root && mkdir compute && cd compute && wget -q https://github.com/intel/compute-runtime/releases/download/19.03.12192/intel-gmmlib_18.4.1_amd64.deb && wget -q https://github.com/intel/compute-runtime/releases/download/19.03.12192/intel-igc-core_19.02.1330_amd64.deb && wget https://github.com/intel/compute-runtime/releases/download/19.03.12192/intel-igc-opencl_19.02.1330_amd64.deb && wget https://github.com/intel/compute-runtime/releases/download/19.03.12192/intel-opencl_19.03.12192_amd64.deb && dpkg -i --force-all *.deb && cd ..
RUN mkdir compute && cd compute && wget https://github.com/intel/compute-runtime/releases/download/19.26.13286/intel-gmmlib_19.2.1_amd64.deb && wget https://github.com/intel/compute-runtime/releases/download/19.26.13286/intel-igc-core_1.0.9-2211_amd64.deb && wget https://github.com/intel/compute-runtime/releases/download/19.26.13286/intel-igc-opencl_1.0.9-2211_amd64.deb && wget https://github.com/intel/compute-runtime/releases/download/19.26.13286/intel-opencl_19.26.13286_amd64.deb && wget https://github.com/intel/compute-runtime/releases/download/19.26.13286/intel-ocloc_19.26.13286_amd64.deb && dpkg -i --force-all *.deb && cd .. && apt clean all && rm -R /compute
RUN git clone https://github.com/intel/clGPU.git && cd clGPU && chmod 755 make.sh && /bin/bash ./make.sh && cd .. && rm -R /clGPU

# AMD ( AMDGPU & ROCm )
# RUN cd / && git clone --recursive https://github.com/twobombs/cudacluster && cd /cudacluster/amd1850 && ./amdgpu-install -y --headless --opencl=legacy && cd / && rm -rf cudacluster/
# RUN apt install libnuma-dev && wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add - && echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list && apt update && apt -o Dpkg::Options::="--force-overwrite" install rocm-dkms && usermod -a -G video root && apt clean all

# NVidia cl libs
RUN add-apt-repository -y ppa:graphics-drivers/dev && apt-get update
# RUN apt-get -o Dpkg::Options::="--force-overwrite" install nvidia-opencl-dev && apt-get clean all

RUN curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey |  apt-key add - 
RUN curl -s -L https://nvidia.github.io/nvidia-docker/ubuntu20.04/nvidia-docker.list | tee /etc/apt/sources.list.d/nvidia-docker.list
RUN apt-get update && apt-get install -y nvidia-docker2 docker.io && apt-get clean all

# NVidia hw integration
RUN mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility,compute

EXPOSE 6080

ENTRYPOINT /root/run
