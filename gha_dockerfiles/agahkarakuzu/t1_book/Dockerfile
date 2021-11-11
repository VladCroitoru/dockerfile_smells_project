FROM jupyter/base-notebook:8ccdfc1da8d5

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential=12.4ubuntu1 \
        emacs \
        git \
        inkscape \
        jed \
        libsm6 \
        libxext-dev \
        libxrender1 \
        lmodern \
        netcat \
        unzip \
        nano \
        curl \
        wget \
        gfortran \
        cmake \
        bsdtar  \
        rsync \
        imagemagick \
        gnuplot-x11 \
        libopenblas-base \
        octave \
        liboctave-dev  \
        octave-info \
        octave-parallel \
        octave-struct \
        octave-io \
        octave-statistics \
        octave-optim \
        octave-image \
        python3-dev \
        ttf-dejavu && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN cd $HOME/work;\
    pip install --upgrade pip --ignore-installed certifi; \
    pip install octave_kernel    \
                sos==0.17.7 \
                sos-notebook==0.17.2 \
                sos-python==0.9.12.1 \
                sos-bash==0.12.3 \
                sos-matlab==0.9.12.1 \
                sos-ruby==0.9.15.0 \
                sos-sas==0.9.12.3 \
                sos-julia==0.9.12.1 \
                sos-javascript==0.9.12.2 \
                sos-r==0.9.12.2 \
                scipy \
                plotly==3.10.0 \
                flask \
                ipywidgets \
                nbconvert==5.4.0 \
                jupyterlab==2.2.0  \
                repo2data; \
    python -m sos_notebook.install;\
    git clone --single-branch -b master https://github.com/qMRLab/t1_book.git;                            \
    cd t1_book;\
    git clone https://github.com/neuropoly/qMRLab.git; \
    cd qMRLab; \
    git checkout 0e97155a6e310911e575ebd8f8870e5f2988a82b; \
    cd ..; \
    mkdir qMRLab/data; \
    for i in _requirements/*_dataset.json; do repo2data -r "$i"; done; \
    chmod -R 777 $HOME/work/t1_book; \
    octave --eval "cd qMRLab; \
                      startup; \
                      pkg list;"

WORKDIR $HOME/work/t1_book

USER $NB_UID

