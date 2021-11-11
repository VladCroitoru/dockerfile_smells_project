FROM centos:7

ENV CENTOS_FRONTEND noninteractive

RUN yum install -y epel-release && \
    yum update -y && \
    yum clean all

RUN yum install -y supervisor build-essential git tar sudo wget make gcc gcc-c++ python-pip python-devel \
    python-msgpack python-daemon

RUN yum install -y numpy
RUN yum install -y scipy

RUN mkdir -p /var/log/skyline /var/run/skyline /var/log/redis /var/dump

RUN wget http://download.redis.io/releases/redis-2.6.16.tar.gz -O /redis.tar.gz && \
    tar xvf /redis.tar.gz && \
    rm -f /redis.tar.gz && \
    mv redis-*.*.* redis && \
    cd /redis && make

ENV PATH $PATH:/redis/src

RUN pip install --upgrade pip
RUN pip install pandas
RUN pip install patsy
RUN pip install statsmodels
RUn pip install msgpack_python

RUN git clone https://github.com/etsy/skyline.git /skyline
RUN pip install -r /skyline/requirements.txt

RUN mkdir -p /var/log/supervisor
COPY ./etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./bin/container-startup.sh /bin/container-startup.sh

VOLUME ["/var/log/skyline","/var/log/redis", "/var/dump"]

EXPOSE 80 2024

CMD ["/bin/container-startup.sh"]

