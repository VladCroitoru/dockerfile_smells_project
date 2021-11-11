FROM ubuntu:14.04

MAINTAINER brunetto ziosi <brunetto.ziosi@gmail.com>

# Public version of StarLab4.4.4, see http://www.sns.ias.edu/~starlab/

ENV DEBIAN_FRONTEND noninteractive

ENV STARLAB_FILE starlabDocker.tar.gz

# Copy StarLab bundle into the image
COPY $STARLAB_FILE /

# This has to be set by hand and MUST be the same of the host
##############
# longisland #
##############
# ENV CUDA_DRIVER 340.46
# ENV CUDA_INSTALL http://us.download.nvidia.com/XFree86/Linux-x86_64/${CUDA_DRIVER}/NVIDIA-Linux-x86_64-${CUDA_DRIVER}.run
# ENV CUDA_TOOLKIT cuda_6.0.37_linux_64.run
# ENV CUDA_TOOLKIT_DOWNLOAD http://developer.download.nvidia.com/compute/cuda/6_0/rel/installers/$CUDA_TOOLKIT
##############
#    uno     #
##############
# ENV CUDA_DRIVER 331.38
# ENV CUDA_INSTALL http://us.download.nvidia.com/XFree86/Linux-x86_64/${CUDA_DRIVER}/NVIDIA-Linux-x86_64-${CUDA_DRIVER}.run
# ENV CUDA_TOOLKIT cuda_5.5.22_linux_64.run
# ENV CUDA_TOOLKIT_DOWNLOAD http://developer.download.nvidia.com/compute/cuda/5_5/rel/installers/$CUDA_TOOLKIT
##############
#   spritz   #
##############
ENV CUDA_DRIVER 331.113
ENV CUDA_INSTALL http://us.download.nvidia.com/XFree86/Linux-x86_64/${CUDA_DRIVER}/NVIDIA-Linux-x86_64-${CUDA_DRIVER}.run
ENV CUDA_TOOLKIT cuda_5.5.22_linux_64.run
ENV CUDA_TOOLKIT_DOWNLOAD http://developer.download.nvidia.com/compute/cuda/5_5/rel/installers/$CUDA_TOOLKIT
################
#  sfursat     #
# to be tested #
################
# ENV CUDA_DRIVER 270.41.19
# ENV CUDA_INSTALL http://us.download.nvidia.com/XFree86/Linux-x86_64/${CUDA_DRIVER}/NVIDIA-Linux-x86_64-${CUDA_DRIVER}.run
# ENV CUDA_TOOLKIT ????
# ENV CUDA_TOOLKIT_DOWNLOAD ????????

# Update and install minimal and clean up packages
RUN apt-get update --quiet && apt-get install --yes \
 --no-install-recommends --no-install-suggests \
 build-essential module-init-tools wget libboost-all-dev   \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

# Install CUDA drivers
RUN wget $CUDA_INSTALL -P /tmp --no-verbose \
      && chmod +x /tmp/NVIDIA-Linux-x86_64-${CUDA_DRIVER}.run \
      && /tmp/NVIDIA-Linux-x86_64-${CUDA_DRIVER}.run -s -N --no-kernel-module \
      && rm -rf /tmp/*

# Install CUDA toolkit
RUN wget $CUDA_TOOLKIT_DOWNLOAD && chmod +x $CUDA_TOOLKIT \
&& ./$CUDA_TOOLKIT -toolkit -toolkitpath=/usr/local/cuda-site -silent -override \
&& rm $CUDA_TOOLKIT

# Set env variables
RUN echo "PATH=$PATH:/usr/local/cuda-site/bin" >> .bashrc          \
&& echo "LD_LIBRARY_PATH=/usr/local/cuda-site/lib64" >> .bashrc   \
&& . /.bashrc \
&& ldconfig /usr/local/cuda-site/lib64

# Install StarLab w/ and w/o GPU, w/ and w/o tidal fields
RUN tar -xvf $STARLAB_FILE && rm $STARLAB_FILE \
&& cp -r starlab starlab-no-GPU               \
&& cp -r starlab starlabAS-no-GPU             \
&& cp -r starlab starlabAS-GPU                \
&& mv starlab starlab-GPU

# Tidal field version only has 5 files different, 
# so we can copy them into a copy of the non TF version:

# ~~starlab/src/node/dyn/util/add_tidal.C~~
# starlab/src/node/dyn/util/dyn_external.C
# ~~starlab/src/node/dyn/util/dyn_io.C~~
# ~~starlab/src/node/dyn/util/set_com.C~~
# ~~starlab/src/node/dyn/util/dyn_story.C~~

RUN cp starlabAS/*.C starlabAS-no-GPU/src/node/dyn/util/ \
&& cp starlabAS/*.C starlabAS-GPU/src/node/dyn/util/     \
&& rm -rf starlabAS

# No longer needed
# && cp starlabAS/dyn.h starlabAS-no-GPU/include/          \
# && cp starlabAS/dyn.h starlabAS-GPU/include/             \


# Compile sapporo
RUN cd sapporo/ && make && bash compile.sh && cd ../

# With and w/o GPU and w/ and w/o AS tidal fields
RUN cd /starlab-GPU/ && ./configure --with-f77=no && make && make install && cd ../ \
&& mv /starlab-GPU/usr/bin slbin-GPU && rm -rf /starlab-GPU \
&& cd /starlabAS-GPU/ && ./configure --with-f77=no && make && make install && cd ../ \
&& mv /starlabAS-GPU/usr/bin slbinAS-GPU && rm -rf /starlabAS-GPU \
&& cd /starlab-no-GPU/ && ./configure --with-f77=no --with-grape=no && make && make install && cd ../ \
&& mv /starlab-no-GPU/usr/bin slbin-no-GPU && rm -rf /starlab-no-GPU \
&& cd /starlabAS-no-GPU/ && ./configure --with-f77=no --with-grape=no && make && make install && cd ../ \
&& mv /starlabAS-no-GPU/usr/bin slbinAS-no-GPU && rm -rf /starlabAS-no-GPU

# Default command.
ENTRYPOINT ["/bin/bash"]

