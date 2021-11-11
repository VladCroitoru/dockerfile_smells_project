from centos

RUN mkdir /work
WORKDIR /work
RUN yum install -y readline-devel openssl-devel wget gcc gcc-c++ make
RUN wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz && tar -xJvf Python-2.7.12.tar.xz && rm -rf Python-2.7.12.tar.xz && \
    cd Python-2.7.12/ && ./configure --prefix=/usr/local/python2.7 &&  make &&  make install && \
    ln -s /usr/local/python2.7/bin/python2.7 /usr/local/bin/python && \
    echo "export PATH=$PATH:/usr/lib64/qt-3.3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/usr/local/python2.7/bin" >> /etc/profile
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum install -y python-pip && pip install -U pip
RUN wget http://www.nagare.org/download/nagare-0.4.1.tar.gz && tar xvf nagare-0.4.1.tar.gz && rm -rf nagare-0.4.1.tar.gz
RUN wget https://pypi.python.org/packages/d4/0c/9840c08189e030873387a73b90ada981885010dd9aea134d6de30cd24cb8/virtualenv-15.1.0.tar.gz && tar xvf virtualenv-15.1.0.tar.gz && rm -rf virtualenv-15.1.0.tar.gz
RUN python virtualenv-15.1.0/virtualenv.py /work/nagare-0.4.1 && /work/nagare-0.4.1/bin/easy_install 'nagare[full]' && \
		echo "export PATH=$PATH:/work/nagare-0.4.1/bin" >> /etc/profile
RUN /work/nagare-0.4.1/bin/easy_install kansha
#RUN /work/nagare-0.4.1/bin/nagare-admin create-db kansha && /work/nagare-0.4.1/bin/kansha-admin alembic-stamp head && \
# 	/work/nagare-0.4.1/bin/kansha-admin create-demo && /work/nagare-0.4.1/bin/kansha-admin create-index

CMD /work/nagare-0.4.1/bin/nagare-admin serve kansha
