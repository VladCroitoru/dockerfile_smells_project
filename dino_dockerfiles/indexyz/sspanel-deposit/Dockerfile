FROM hyalx/centos:centos6

RUN mkdir /usr/app

COPY . /usr/app

RUN yum install epel-release -y && \
    yum install python-setuptools -y && \
    easy_install pip && \
    pip install -r /usr/app/requirements.txt

WORKDIR ["/usr/app"]

EXPOSE "5000/tcp"

ENTRYPOINT ["python"]
CMD ["/usr/app/Alipay-Panel.py"]
