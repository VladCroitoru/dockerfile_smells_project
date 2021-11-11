# cuda80-fix + cudnn7
#
# VERSION               0.0.1

# 
# 8.0/devel/cudnn7/Dockerfile · ubuntu16.04 · nvidia / cuda · GitLab
# https://gitlab.com/nvidia/cuda/blob/ubuntu16.04/8.0/devel/cudnn7/Dockerfile
# 

FROM      nvidia/cuda:8.0-cudnn7-devel-ubuntu16.04
LABEL     maintainer="allen7575@gmail.com"

##
## Ubuntu - Packages - Search
## https://packages.ubuntu.com/search?suite=xenial&section=all&arch=amd64&searchon=contents&keywords=Search
##

############
# update package list
############
RUN apt-get update

##############################
#########################
## fix
#########################
##############################

###
### solve for
### >>> WARNING - libGL.so not found, refer to CUDA Getting Started Guide for how to find and install them. <<<
### >>> WARNING - libX11.so not found, refer to CUDA Getting Started Guide for how to find and install them. <<<
### >>> WARNING - Xlib.h not found, refer to CUDA Getting Started Guide for how to find and install them. <<<
### >>> WARNING - gl.h not found, refer to CUDA Getting Started Guide for how to find and install them. <<<
###
### 2_Graphics/volumeFiltering
### 2_Graphics/simpleGL
### 2_Graphics/bindlessTexture
### 2_Graphics/volumeRender
### 2_Graphics/Mandelbrot
### 2_Graphics/marchingCubes
### 2_Graphics/simpleTexture3D
### 3_Imaging/imageDenoising
### 3_Imaging/recursiveGaussian
### 3_Imaging/simpleCUDA2GL
### 3_Imaging/postProcessGL
### 3_Imaging/bicubicTexture
### 3_Imaging/boxFilter
### 3_Imaging/SobelFilter
### 3_Imaging/cudaDecodeGL
### 3_Imaging/bilateralFilter
### 5_Simulations/particles
### 5_Simulations/smokeParticles
### 5_Simulations/oceanFFT
### 5_Simulations/fluidsGL
### 5_Simulations/nbody
### 6_Advanced/FunctionPointers
### 7_CUDALibraries/randomFog
###
RUN apt-get install -y libgl1-mesa-dev

###
### solve for
### >>> WARNING - libGLU.so not found, refer to CUDA Getting Started Guide for how to find and install them. <<<
### >>> WARNING - glu.h not found, refer to CUDA Getting Started Guide for how to find and install them. <<<
###
RUN apt-get install -y libglu1-mesa-dev

###
### solve for
### /usr/bin/ld: cannot find -lglut
### https://stackoverflow.com/questions/15064159/usr-bin-ld-cannot-find-lglut
###
RUN apt-get install -y freeglut3-dev

###
### solve for
### >>> WARNING - egl.h not found, please install egl.h <<<
### >>> WARNING - eglext.h not found, please install eglext.h <<<
### >>> WARNING - gl31.h not found, please install gl31.h <<<
###
### 2_Graphics/simpleGLES_EGLOutput
### 2_Graphics/simpleGLES
### 2_Graphics/simpleGLES_screen
### 5_Simulations/nbody_opengles
### 5_Simulations/fluidsGLES
### 5_Simulations/nbody_screen
###
RUN apt-get install -y libgles2-mesa-dev


###
### You should also search 'UBUNTU_PKG_NAME = "nvidia-367"' and replace it to 'UBUNTU_PKG_NAME = "nvidia"'
### for all matched files in the NVIDIA_CUDA-8.0_Samples folder to make it works.
###
RUN mkdir /usr/lib/nvidia && \
    `### solve for  /usr/bin/ld: cannot find -lnvcuvid` \
    `### 3_Imaging/cudaDecodeGL` \
    ln -s /usr/local/nvidia/lib64/libnvcuvid.so.1 /usr/lib/nvidia/libnvcuvid.so && \
    `### solve for >>> WARNING - libEGL.so not found, please install libEGL.so <<<` \
    `### 3_Imaging/EGLStreams_CUDA_Interop `\
    ln -s /usr/local/nvidia/lib64/libEGL.so.1 /usr/lib/nvidia/libEGL.so && \
    `### solve for >>> WARNING - libGLES.so not found, please install libGLES.so <<<` \
    `### 2_Graphics/simpleGLES_EGLOutput` \
    `### 2_Graphics/simpleGLES` \
    `### 2_Graphics/simpleGLES_screen` \
    `### 5_Simulations/nbody_opengles` \
    `### 5_Simulations/fluidsGLES` \
    `### 5_Simulations/nbody_screen` \
    ln -s /usr/local/nvidia/lib64/libGLESv2_nvidia.so.2 /usr/lib/nvidia/libGLESv2.so


##############################
#########################
## Tools
#########################
##############################

# ##########
# # install vim
# ##########
# RUN apt-get install -y vim

##############################
#########################
## ssh daemon
#########################
##############################

# ###################
# # install ssh
# ###################
# RUN apt-get install -y ssh

# # enable ssh root login
# # 技术|Linux有问必答：如何修复“X11 forwarding request failed on channel 0”错误
# # https://linux.cn/article-4014-1.html
# RUN sed -i "s/PermitRootLogin/# PermitRootLogin/g" /etc/ssh/sshd_config && \
#     echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
#     sed -i "s/X11UseLocalhost/# X11UseLocalhost/g" /etc/ssh/sshd_config && \
#     echo "X11UseLocalhost no" >> /etc/ssh/sshd_config

# # change password with username:password
# RUN echo root:root | chpasswd

# # first start to preserve all SSH host keys
# RUN service ssh start

# #################
# # install sshfs
# #################
# RUN apt-get install -y sshfs

# # make dir for mount point use
# RUN mkdir ~/client-sshfs-project

# ##############################
# #########################
# ## X11 forward GUI
# #########################
# ##############################

# #############
# # install xeyes, xclock
# #############
# RUN apt-get install -y x11-apps

# ###################
# # install VirtualGL
# ###################
# # nvidia-virtualgl/Dockerfile at master · plumbee/nvidia-virtualgl
# # https://github.com/plumbee/nvidia-virtualgl/blob/master/Dockerfile

# # install mesa-utils for testing glxgear
# RUN apt-get install -y mesa-utils

# # install curl for download VirtualGL
# RUN apt-get install -y curl

# # download & install VirtualGL
# ENV VIRTUALGL_VERSION 2.5.2
# RUN curl -sSL https://downloads.sourceforge.net/project/virtualgl/"${VIRTUALGL_VERSION}"/virtualgl_"${VIRTUALGL_VERSION}"_amd64.deb -o virtualgl_"${VIRTUALGL_VERSION}"_amd64.deb && \
#     dpkg -i virtualgl_*_amd64.deb && \
#     rm virtualgl_*_amd64.deb

# # install libxv1 to avoid
# # glxgears: error while loading shared libraries: libXv.so.1: cannot open shared object file: No such file or directory
# # when executed vglrun glxgears
# RUN apt-get install -y libxv1

# # Granting Access to the 3D X Server
# # https://cdn.rawgit.com/VirtualGL/virtualgl/2.5.2/doc/index.html#hd006001
# #RUN /opt/VirtualGL/bin/vglserver_config -config +s +f -t


##############################
#########################
## nvidia-docker
#########################
##############################

#####################
# add nvcc PATH for ssh interactive
# unix - How do I set $PATH such that `ssh user@host command` works? - Stack Overflow 
# https://stackoverflow.com/questions/940533/how-do-i-set-path-such-that-ssh-userhost-command-works
#####################
#RUN sed -i '/interactively/ i export PATH=$PATH:/usr/local/cuda-8.0/bin\n' /root/.bashrc

# Newby question to CUDA container and ssh · Issue #36 · NVIDIA/nvidia-docker 
# https://github.com/NVIDIA/nvidia-docker/issues/36
#RUN echo "export PATH=\$PATH" >> /etc/profile && \
#    echo "ldconfig" >> /etc/profile

# ####################
# # nvidia-docker links
# ####################
# # Image inspection · NVIDIA/nvidia-docker Wiki
# # https://github.com/NVIDIA/nvidia-docker/wiki/Image-inspection#nvidia-docker
# # when nvidia-docker run is used, we inspect the image specified on the command-line. In this image,
# # we lookup the presence and the value of the label com.nvidia.volumes.needed

# # if you are using nvidia driver, you need to add this to avoid
# # libGL error: failed to load driver: swrast
# LABEL com.nvidia.volumes.needed="nvidia_driver"
# ENV PATH /usr/local/nvidia/bin:${PATH}
# ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}

# # set PATH & LD_LIBRARY_PATH env variable for ssh login session
# # Env variable cannot be passed to container - General Discussions - Docker Forums
# # https://forums.docker.com/t/env-variable-cannot-be-passed-to-container/5298/6
# RUN echo 'export PATH=/usr/local/nvidia/bin:$PATH' >> /etc/profile.d/nvidia.sh && \
#     echo 'export LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH' >> /etc/profile.d/nvidia.sh


##############
# upgrade
##############
RUN apt-get upgrade -y

##############
# cleanup
##############
# debian - clear apt-get list - Unix & Linux Stack Exchange
# https://unix.stackexchange.com/questions/217369/clear-apt-get-list
#
# bash - autoremove option doesn't work with apt alias - Ask Ubuntu
# https://askubuntu.com/questions/573624/autoremove-option-doesnt-work-with-apt-alias
#
RUN apt-get autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# EXPOSE 22
CMD    ["bash"]


