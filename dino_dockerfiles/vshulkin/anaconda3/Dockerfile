FROM debian:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN apt-get install -y curl grep sed dpkg procps && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

RUN pip install --upgrade pip && \
    pip install ipyparallel && \
    conda update -n base conda && \    
    conda config --add channels conda-forge && \
    conda install --channel anaconda-nb-extensions nbbrowserpdf && \
    conda install nb_conda_kernels && \
    conda install -c conda-forge jupyter_contrib_nbextensions && \
    conda create -n py36 python=3.6 ipykernel && \
    conda create -n py27 python=2.7 ipykernel && \
    conda install jupyter -y --quiet && \
    mkdir /opt/notebooks

RUN ipcluster nbextension enable 

RUN [ "/bin/bash", "-c", "source activate py27 && pip install sslyze netaddr" ] && \
    pip install --upgrade pip && \
    pip install sslyze netaddr
    
ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]

