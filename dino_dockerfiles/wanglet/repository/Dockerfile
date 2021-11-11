FROM centos:7.4.1708

RUN rm -rf /etc/yum.repos.d/* \
    && curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo \
    && curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo \
    && yum -y install python-pip gcc python-devel libffi-devel openssl-devel vim wget createrepo mysql-devel \
    && rm -rf /var/cache/*

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade pip setuptools pip2pi

RUN mkdir /sources /repository

WORKDIR /repository
