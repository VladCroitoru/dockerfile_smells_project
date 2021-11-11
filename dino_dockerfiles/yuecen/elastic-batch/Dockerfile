FROM ubuntu:latest
MAINTAINER yuecen <yuecendev+docker@gmail.com>
VOLUME ["/root"]
WORKDIR /root
RUN build_deps="python-dev build-essential" && \
    apt-get update -y && apt-get install -y python-pip ${build_deps} && \
    pip install pip -U && \
    pip install elasticsearch && \
    pip install pandas && \
    pip install python-dateutil && \
    pip install slacker && \
    pip install ascii_graph && \
    pip install terminaltables && \
    apt-get purge -y --auto-remove ${build_deps} && \
    apt-get autoremove -y

CMD ["python"]
