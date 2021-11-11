FROM ubuntu:14.04
MAINTAINER Dimitri Saingre <dimitrisaingre@orange.fr>
MAINTAINER Anaël CHARDAN <anael.chardan@gmail.com>


RUN apt-get update && apt-get install -y curl build-essential emacs \
    && curl -sSL -o pvs.tgz -O http://pvs.csl.sri.com/cgi-bin/download.cgi\?file\=pvs-6.0-ix86_64-Linux-allegro.tgz\&accept\=I+accept \
    && mkdir pvs \
    && tar -xzf pvs.tgz -C /pvs \
    && sed -i 's#PVSPATH=/home/owre/pvs.git#PVSPATH=/pvs#' /pvs/pvs \
    && sed -i 's#PVSPATH=/home/owre/pvs.git#PVSPATH=/pvs#' /pvs/proveit \
    && sed -i 's#PVSPATH=/home/owre/pvs.git#PVSPATH=/pvs#' /pvs/pvsio \
    && sed -i 's#PVSPATH=/home/owre/pvs.git#PVSPATH=/pvs#' /pvs/provethem \
    && chmod u+w /pvs/pvs /pvs/pvsio /pvs/proveit /pvs/provethem \
    && chmod a+x /pvs/pvs /pvs/pvsio /pvs/proveit /pvs/provethem \
    && echo "alias pvs=\"/pvs/pvs\"" >> /root/.bashrc \
    && echo "echo \"Welcome in PVS docker\"" >> /root/.bashrc \
    && echo "echo \"run $ pvs to launch PVS\"" >> /root/.bashrc


WORKDIR /home/work
