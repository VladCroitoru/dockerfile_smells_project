FROM phusion/holy-build-box-64

# Install EPL
ADD http://download.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm /
RUN rpm -i --quiet /epel-release-5-4.noarch.rpm
RUN rm -f /epel-release-5-4.noarch.rpm

# Install prerequisites
#RUN yum install -y --quiet wget clang gcc gcc-c++ git scons redhat-lsb kernel-devel dkms cmake doxygen
RUN yum install -y --quiet dkms libvdpau git wget

# Install TeX
ADD http://ctan.mackichan.com/systems/texlive/tlnet/install-tl-unx.tar.gz /
ADD https://raw.githubusercontent.com/omnia-md/virtual-machines/master/linux/texlive.profile /
RUN tar -xzf /install-tl-unx.tar.gz
RUN cd install-tl-*; ./install-tl -profile /texlive.profile; cd -
RUN rm -rf /install-tl-unx.tar.gz install-tl-* /texlive.profile
ENV PATH=/usr/local/texlive/2015/bin/x86_64-linux:$PATH

# Install CUDA
ADD http://developer.download.nvidia.com/compute/cuda/7_0/Prod/local_installers/rpmdeb/cuda-repo-rhel6-7-0-local-7.0-28.x86_64.rpm /
RUN rpm --quiet -i /cuda-repo-rhel6-7-0-local-7.0-28.x86_64.rpm
RUN RM -f /cuda-repo-rhel6-7-0-local-7.0-28.x86_64.rpm
RUN yum clean -y --quiet expire-cache
RUN yum install -y --quiet cuda-core-7-0-7.0-28.x86_64 cuda-cufft-dev-7-0-7.0-28.x86_64 cuda-cudart-dev-7-0-7.0-28.x86_64
RUN rpm --quiet --nodeps -Uvh /var/cuda-repo-7-0-local/xorg-x11-drv-nvidia-libs-346.46-1.el6.x86_64.rpm
RUN rpm --quiet --nodeps -Uvh /var/cuda-repo-7-0-local/xorg-x11-drv-nvidia-devel-346.46-1.el6.x86_64.rpm
RUN ln -s /usr/include/nvidia/GL/  /usr/local/cuda-7.0/include/
RUN yum clean -y --quiet all

# Install CUDA
#ENV CUDA_HOME=/usr/local/cuda-7.0 CUDA_LIBPATH=/usr/local/cuda-7.0/lib64
#ADD http://developer.download.nvidia.com/compute/cuda/repos/rhel6/x86_64/cuda-repo-rhel6-7.0-28.x86_64.rpm .
#RUN rpm -i --quiet cuda-repo-rhel6-7.0-28.x86_64.rpm
#RUN yum clean expire-cache
#RUN yum install -y --quiet cuda

# Install AMD SDK for OpenCL
ENV OPENCL_HOME=/opt/AMDAPPSDK-2.9-1 OPENCL_LIBPATH=/opt/AMDAPPSDK-2.9-1/lib/x86_64
ADD http://jenkins.choderalab.org/userContent/AMD-APP-SDK-linux-v2.9-1.599.381-GA-x64.tar.bz2 /
RUN tar xjf /AMD-APP-SDK-linux-v2.9-1.599.381-GA-x64.tar.bz2
RUN /AMD-APP-SDK-v2.9-1.599.381-GA-linux64.sh -- -s -a yes
RUN rm -f AMD-APP-SDK-v2.9-1.599.381-GA-linux64.sh

# Install Boost.
ENV BOOST_PKG=boost_1_55_0 BOOST_SOURCE=$HOME/boost_1_55_0
RUN wget --quiet http://downloads.sourceforge.net/project/boost/boost/1.55.0/boost_1_55_0.tar.bz2
RUN tar xjf $BOOST_PKG.tar.bz2 $BOOST_PKG/libs/regex $BOOST_PKG/libs/filesystem $BOOST_PKG/libs/system $BOOST_PKG/libs/iostreams $BOOST_PKG/boost

# Build OpenSSL (already installed)
#ENV OPENSSL_HOME=$HOME/openssl-1.0.2d
#RUN wget https://www.openssl.org/source/openssl-1.0.2d.tar.gz
#RUN tar zxf openssl-1.0.2d.tar.gz
#RUN cd openssl-1.0.2d ; ./config no-shared ; make
