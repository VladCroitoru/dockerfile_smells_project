FROM centos:7.3.1611

MAINTAINER Xu Hui <xuhui546@hotmail.com>

ENV LANG=en_US.UTF-8

RUN yum install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

ENV PATH /opt/conda/bin:$PATH
ENV JUPYTER_PORT 8888
ENV JUPYTER_PASS ''
ENV JUPYTER_WORKDIR /

ADD ./cfg_notebook.py /root
RUN echo $'python /root/cfg_notebook.py -l ${JUPYTER_PORT} -p "${JUPYTER_PASS}" >& 1 \n\
jupyter notebook --notebook-dir=${JUPYTER_WORKDIR} --allow-root --no-browser >& 1 \n\
/bin/bash \n\
exit 0'>>/etc/rc.d/rc.local

RUN chmod +x /etc/rc.d/rc.local

CMD /bin/bash /etc/rc.local


