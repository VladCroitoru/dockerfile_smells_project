# Created on Jan, 17, 2017
# @author: Yvictor

FROM yvictor/docker_conda:cmpy
MAINTAINER yvictor

WORKDIR /home
COPY . /winesc
RUN conda install jupyter notebook -y
CMD jupyter notebook --ip 0.0.0.0
