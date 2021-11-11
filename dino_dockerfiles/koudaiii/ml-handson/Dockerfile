FROM centos:6.6
ENV PATH $PATH:/opt/miniconda3/bin

RUN echo "nameserver 172.17.42.1" > /etc/resolv.conf
RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf
RUN yum -y update

RUN yum groupinstall -y "Development tools"
RUN yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel

RUN yum install -y tar wget

RUN curl -O https://www.python.org/ftp/python/3.3.3/Python-3.3.3.tgz; \
    tar zxf Python-3.3.3.tgz; \
    cd Python-3.3.3; \
    ./configure --prefix=/opt/local; \
    make && make altinstall


RUN wget -qO- https://bootstrap.pypa.io/get-pip.py | python
RUN wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -P /tmp/
RUN bash /tmp/Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3

RUN yes | pip install virtualenv
RUN yes | /opt/miniconda3/bin/conda create -n ml_env numpy scipy scikit-learn matplotlib cython ipython ipython-notebook
RUN rm /tmp/Miniconda3-latest-Linux-x86_64.sh


RUN source /opt/miniconda3/envs/ml_env/bin/activate ml_env; \
    ipython profile create nbserver

RUN rm ~/.ipython/profile_nbserver/ipython_notebook_config.py
ADD ipython_notebook_config.py /root/.ipython/profile_nbserver/ipython_notebook_config.py
ADD start.sh /root/start.sh
RUN chmod a+x /root/start.sh
ADD server.sh /root/server.sh
RUN chmod a+x /root/server.sh

CMD ["/root/start.sh"]
