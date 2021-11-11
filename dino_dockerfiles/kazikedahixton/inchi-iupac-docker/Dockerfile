#
# Docker container for inchi-1 from iupac
#
FROM ubuntu
MAINTAINER Kazuyoshi Ikeda, kazikeda@me.com

# Install packages
RUN apt-get update && \
    apt-get install -y wget unzip gcc g++ make

# Install inchi-1 from iupac
RUN cd /opt && \
    wget http://www.iupac.org/fileadmin/user_upload/publications/e-resources/inchi/1.03/INCHI-1-API.zip && \
    unzip INCHI-1-API.zip && \
    cd /opt/INCHI-1-API/INCHI/gcc/inchi-1 && \
    make && \
    ln -s /opt/INCHI-1-API/INCHI/gcc/inchi-1/inchi-1 /usr/local/inchi-1 && \
    rm /opt/INCHI-1-API.zip

CMD ["/opt/INCHI-1-API/INCHI/gcc/inchi-1/inchi-1"]
