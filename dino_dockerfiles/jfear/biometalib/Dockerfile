FROM jfear/centos7-miniconda3:py3.6

MAINTAINER Justin Fear <justin.m.fear@gmail.com>

RUN conda install -y biometalib && \
    conda clean --all -y

CMD ["/bin/bash"]
