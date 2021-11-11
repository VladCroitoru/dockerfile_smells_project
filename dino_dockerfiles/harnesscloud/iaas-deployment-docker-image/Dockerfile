FROM harnesscloud/iaas-deployment-base:latest

MAINTAINER Gabriel Figueiredo <gabriel.figueiredo@imperial.ac.uk>

WORKDIR /harness

RUN git clone https://github.com/harnesscloud/crs.git
RUN git clone https://github.com/harnesscloud/harness-resource-manager.git
RUN git clone https://github.com/harnesscloud/irm-nova.git
RUN git clone https://github.com/harnesscloud/irm-neutron.git
RUN git clone https://github.com/harnesscloud/irm-net.git

COPY cfg/* cfg/
COPY supervisord.conf ./
COPY start_harness_iaas ./
COPY bootstrap ./

EXPOSE 56789 8889 7779 9999

CMD ./start_harness_iaas
