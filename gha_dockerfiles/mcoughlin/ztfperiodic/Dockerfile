#FROM debian:stable-slim
FROM docker.io/nvidia/cuda:10.1-devel-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=linux

RUN apt-get update && \
    apt-get -y install --no-install-recommends openssh-client && \
    apt-get -y install vim && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get -y install \
    cython3 \
    gfortran \
    git \
    python3-astroplan \
    python3-astropy \
    python3-astroquery \
    python3-dateutil \
    python3-f2py \
    python3-future \
    python3-healpy \
    python3-h5py \
    python3-matplotlib \
    python3-numpy \
    python3-pandas \
    python3-pip \
    python3-pyvo \
    python3-scipy \
    python3-seaborn \
    python3-tqdm \
    rsync && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/stubs/libcuda.so.1
ENV LD_LIBRARY_PATH "/usr/local/cuda/lib64/stubs/:${LD_LIBRARY_PATH}$"

# Install requirements. Do this before installing our own package, because
# presumably the requirements change less frequently than our own code.
COPY requirements.txt /
RUN pip3 install --no-cache-dir -r \
    /requirements.txt \
    git+https://github.com/ejaszewski/periodfind.git
RUN rm /requirements.txt

COPY . /src
RUN pip3 install --no-cache-dir /src

RUN useradd -mr ztfperiodic
RUN echo "ztfperiodic ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
ENV HOME /home/ztfperiodic

#COPY id_rsa $HOME/.ssh/id_rsa
#COPY docker/etc/ssh/ssh_known_hosts $HOME/.ssh/known_hosts
COPY docker/penquins/penquins.py /usr/local/lib/python3.6/dist-packages/penquins/ 
RUN chown -R ztfperiodic:ztfperiodic $HOME
#RUN \
#    chmod 700 $HOME/.ssh &&\
#    chmod 600 $HOME/.ssh/id_rsa

USER ztfperiodic:ztfperiodic
WORKDIR /home/ztfperiodic
#RUN mkdir -p /home/ztfperiodic/ids

#RUN ssh-keygen -f "/home/ztfperiodic/.ssh/known_hosts" -R "schoty.caltech.edu"

ENV LD_LIBRARY_PATH "/usr/local/cuda/lib64"

#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["python3","/src/bin/ztfperiodic_period_search.py"]
