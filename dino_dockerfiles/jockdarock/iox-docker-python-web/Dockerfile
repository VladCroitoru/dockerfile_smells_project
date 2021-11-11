FROM python:3-alpine

RUN pip3 install bottle

EXPOSE 8000

COPY main.py /main.py
COPY config.py /config.py
COPY package_config.ini /package_config.ini

LABEL cisco.info.name="iox_docker_python_web" \
      cisco.info.description="Basic WebApp for IOx" \
      cisco.info.version="0.21" \
      cisco.info.author-link="" \
      cisco.info.author-name="" \
      cisco.type=docker \
      cisco.cpuarch=x86_64 \
      cisco.resources.profile=custom \
      cisco.resources.cpu=100 \
      cisco.resources.memory=100 \
      cisco.resources.disk=10 \
      cisco.resources.network.0.interface-name=eth0 \
      cisco.resources.network.0.ports.tcp=[8000]

CMD ["/usr/local/bin/python", "/main.py"]