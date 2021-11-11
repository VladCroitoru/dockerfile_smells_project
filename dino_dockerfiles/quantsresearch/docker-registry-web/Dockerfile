FROM centos:7
MAINTAINER QR Developers <sugiyasu@qri.jp>


# create user
RUN useradd -d /home/web -m web


RUN yum update -y
RUN yum install -y wget gcc zlib-devel openssl-devel rsync make


# install python 3
WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz && tar xzf Python-3.5.0.tgz
RUN cd Python-3.5.0 && ./configure --with-zlib-dir=/usr/lib64 && make install
RUN ln -fs /usr/local/bin/python3 /bin/python
RUN ln -fs /usr/local/bin/pip3 /bin/pip


RUN pip install bottle


ADD web /var/local/web
EXPOSE 8080
WORKDIR /var/local/web/
ENTRYPOINT ["python", "main.py"]
USER web
