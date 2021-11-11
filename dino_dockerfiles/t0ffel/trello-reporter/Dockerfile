FROM centos/python-34-centos7:latest

RUN yum update -y && yum clean all

RUN yum install -y python3 \
                   python3-pip \
                   git

RUN git clone https://github.com/t0ffel/trello-reporter.git /opt/app-root/src

VOLUME /opt/app-root/src/app/secrets/

RUN pip3 install -r /opt/app-root/src/requirements.txt

WORKDIR /opt/app-root/src/app/
CMD ["python3", "run-reporter.py"]

