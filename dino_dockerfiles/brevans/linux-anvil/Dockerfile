FROM centos:6

MAINTAINER Ben Evans <b.evans@yale.edu>


# Set environment variables
ENV LANG en_US.UTF-8

# Resolves a nasty NOKEY warning that appears when using yum.
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6

# Install basic requirements.
RUN yum update -y && \
    yum install -y \
                   bzip2 \
                   make \
                   patch \
                   tar \
                   which \
                   libXext-devel \
                   libXrender-devel \
                   libSM-devel \
                   libX11-devel \
                   mesa-libGL-devel && \
    yum clean all

# Install devtoolset 2.
# add conda to path after enabling devtoolset-2
RUN yum update -y && \
    yum install -y centos-release-scl yum-utils && \
    yum-config-manager --add-repo http://people.centos.org/tru/devtools-2/devtools-2.repo && \
    yum update -y && \
    yum install -y devtoolset-2-binutils devtoolset-2-gcc devtoolset-2-gcc-c++ && \
    yum clean all 

# Install the latest Miniconda with Python 3 and update everything.
RUN curl -s -L https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh > miniconda.sh && \
    openssl md5 miniconda.sh | grep bec6203dbb2f53011e974e9bf4d46e93 && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh && \
    touch /opt/conda/conda-meta/pinned && \
    export PATH=/opt/conda/bin:${PATH} && \
    conda config --set show_channel_urls True && \
    conda config --add channels conda-forge && \
    conda update --all --yes && \
    conda clean -tipy

# Install conda build and deployment tools.
RUN export PATH=/opt/conda/bin:${PATH} && \
    conda install --yes conda-build anaconda-client jinja2 setuptools && \
    conda install --yes git && \
    conda clean -tipsy

COPY entrypoint /opt/linux-anvil/entrypoint

# Provide a default command (`bash`), which will start if the user doesn't specify one.
ENTRYPOINT ["/opt/linux-anvil/entrypoint"]
CMD ["/bin/bash"]
