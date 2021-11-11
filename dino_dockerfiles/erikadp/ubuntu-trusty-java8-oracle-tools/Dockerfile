FROM erikadp/ubuntu-trusty-ant

ADD dependencies /assets
RUN /assets/setup.sh

# Add Oracle envs
ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe
ENV ORACLE_SID XE
ENV PATH ${PATH}:${ORACLE_HOME}/bin