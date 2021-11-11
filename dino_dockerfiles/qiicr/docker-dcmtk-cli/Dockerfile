FROM fedorov/docker-centos-build
MAINTAINER http://github.com/QIICR

WORKDIR /usr/src
RUN git clone https://github.com/qiicr/docker-dcmtk-cli.git

RUN git clone git://git.dcmtk.org/dcmtk && \
  mkdir dcmtk-build && \
  cd dcmtk-build && \
  cmake -DDCMTK_ENABLE_BUILTIN_DICTIONARY:BOOL=ON -DCMAKE_BUILD_TYPE=Release ../dcmtk && \
  make 

RUN  chmod a+x /usr/src/docker-dcmtk-cli/docker_entry.sh

ENTRYPOINT ["/bin/bash","/usr/src/docker-dcmtk-cli/docker_entry.sh"]
