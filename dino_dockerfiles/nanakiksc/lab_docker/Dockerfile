FROM ubuntu:trusty

RUN apt-get update && apt-get install -y \
    emacs=45.0* \
    gcc=4:4.8.2-1* \
    git=1:1.9.1-1* \
    make=3.81-8.2* \
    python=2.7.5-5* \
    python-dev=2.7.5-5* \
    r-base=3* \
    vim=2:7.4.052-1* \
    wget=1.15-1* \
    exuberant-ctags=1:5.9* \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Add lab software.
RUN git clone https://github.com/ezorita/seeq.git && \
    make -C seeq && \
    cd seeq && \
    python setup.py install && \
    cd ..
RUN git clone https://github.com/gui11aume/starcode.git && \
    make -C starcode
RUN git clone https://github.com/nanakiksc/zerone.git && \
    make -C zerone && \
    R CMD INSTALL zerone/ZeroneRPackage && \
    make clean -C zerone/ZeroneRPackage/src

# Add GEM.
ENV GEM_RELEASE=3 GEM=GEM-binaries-Linux-x86_64-core_i3-20130406-045632
RUN wget -nv http://downloads.sourceforge.net/project/gemlibrary/gem-library/Binary%20pre-release%20${GEM_RELEASE}/${GEM}.tbz2 && \
    tar -xjf ${GEM}.tbz2 && \
    rm ${GEM}.tbz2
# md5sum 06de0a815f0cee963ec94321d899042a

# Add BWA.
RUN git clone https://github.com/lh3/bwa.git && \
    make -C bwa

# Add links to executables.
RUN ln -s /seeq/seeq /usr/local/bin/ && \
    ln -s /starcode/starcode /usr/local/bin/ && \
    ln -s /zerone/zerone /usr/local/bin/ && \
    ln -s /${GEM}/bin/compute-transcriptome /usr/local/bin/ && \
    ln -s /${GEM}/bin/gem* /usr/local/bin/ && \
    ln -s /${GEM}/bin/gtf-2-junctions /usr/local/bin/ && \
    ln -s /${GEM}/bin/splits-2-junctions /usr/local/bin/ && \
    ln -s /${GEM}/bin/transcriptome-2-genome /usr/local/bin/ && \
    ln -s /bwa/bwa /usr/local/bin/
