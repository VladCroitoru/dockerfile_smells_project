FROM hadrieng/docker_base

MAINTAINER Magdalena Arnal <marnal@imim.es>

#Download and install mothur v1.39.1
RUN wget https://github.com/mothur/mothur/releases/download/v1.39.1/Mothur.linux_64.zip
RUN unzip Mothur.linux_64.zip && rm Mothur.linux_64.zip && rm -rf __MACOSX

#Add executable to the path
ENV PATH /mothur:$PATH
