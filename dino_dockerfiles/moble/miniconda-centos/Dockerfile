## This container is similar to the official miniconda container
## <https://hub.docker.com/r/continuumio/miniconda/~/dockerfile/>, but is based on centos6 so that
## we can use the same commands as in the (centos-based) manylinux1 container, while also supporting
## conda builds on the oldest platform conda supports (centos6).
##
## Note that the official miniconda container uses `tini` as the entrypoint.  I believe this is
## because jupyter needs a PID reaper:
##     <http://jupyter-notebook.readthedocs.io/en/stable/public_server.html#docker-cmd>
## I do not intend to run jupyter on this container, so I don't use it.  However, it could be
## added by basing off of `krallin/centos-tini:6` instead of `centos:6`.

FROM centos:6

### Install miniconda2 <https://hub.docker.com/r/continuumio/miniconda/~/dockerfile/>
RUN yum install -y wget bzip2 git curl grep sed dpkg gcc gcc-c++ && \
    mkdir -p /code && \
    echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm -f ~/miniconda.sh && \
    /opt/conda/bin/conda install -y -q -n root conda-build anaconda-client && \
    /opt/conda/bin/conda clean -y -a
ENV PATH /opt/conda/bin:$PATH

CMD [ "/bin/bash" ]
