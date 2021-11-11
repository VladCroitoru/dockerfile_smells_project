FROM centos:centos7
MAINTAINER chris060986@github.com

VOLUME /var/data

USER root

RUN yum clean all && \
        yum -y install epel-release && \
        yum install -y openssh python-pip python-wheel python-virtualenv && \
        pip install --upgrade pip

RUN curl -SL https://github.com/elastic/beats/archive/v5.6.2.tar.gz \
    | tar -xz -C /opt/

WORKDIR /opt/beats-5.6.2/dev-tools/

RUN virtualenv env
RUN . env/bin/activate
RUN pip install -r requirements.txt

RUN . env/bin/activate

WORKDIR /opt/beats-5.6.2/filebeat/

# export
#CMD python ../dev-tools/export_dashboards.py --url ${elasticsearch_url} --regex ${regex} --kibana ${kibana} --dir ${dir}
ENTRYPOINT ["python", "../dev-tools/export_dashboards.py"]
CMD ["--url", "http://localhost:9200", "--regex", "'.*'", "--kibana", ".kibana", "--dir", "/var/data"]
