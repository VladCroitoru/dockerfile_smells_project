FROM python:3

ENV path /opt/gallium

ADD . ${path}
#RUN pip install -U pip
RUN pip install -q ${path}
RUN echo 'StrictHostKeyChecking no' >> /etc/ssh/ssh_config

WORKDIR ${path}

ENTRYPOINT ["gallium"]
