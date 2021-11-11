FROM atecon/gretl

ENV HOME /home/abc

RUN mkdir -p ${HOME}/repo

COPY . ${HOME}/repo

WORKDIR ${HOME}/repo

ENTRYPOINT ['/bin/bash']
