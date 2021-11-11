FROM ubuntu:16.04

MAINTAINER Erik van den Bergh, Earlham Institute, Norwich

RUN apt update && apt install -y \
                            wget \
			    rsync \
			    net-tools

RUN useradd -m admin

RUN mkdir /opt/smrtanalysis
RUN chown admin:admin /opt/smrtanalysis

USER admin
WORKDIR /home/admin

RUN wget -nv http://files.pacb.com/software/smrtanalysis/2.3.0/smrtanalysis_2.3.0.140936.run
RUN wget -nv https://s3.amazonaws.com/files.pacb.com/software/smrtanalysis/2.3.0/smrtanalysis-patch_2.3.0.140936.p5.run

RUN bash smrtanalysis_2.3.0.140936.run -p smrtanalysis-patch_2.3.0.140936.p5.run --rootdir /opt/smrtanalysis --ignore-syscheck --jmstype NONE --batch

RUN rm -rf *

RUN mkdir /home/admin/scripts
COPY scripts/* /home/admin/scripts/

USER root

RUN chown admin:admin /home/admin/scripts/*
RUN chmod ugo+w -R /tmp
#RUN chmod ugo+w -R /opt/smrtanalysis

RUN usermod -d /tmp nobody

USER admin

ENTRYPOINT ["/home/admin/scripts/runRenSeq.sh"]
