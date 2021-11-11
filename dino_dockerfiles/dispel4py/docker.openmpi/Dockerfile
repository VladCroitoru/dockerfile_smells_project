# Build this image:  docker build -t mpi .
#

FROM ubuntu:14.04
MAINTAINER Ole Weidner <ole.weidner@ed.ac.uk>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y openssh-server python-mpi4py python-numpy \
            python-virtualenv python-scipy gcc gfortran openmpi-checkpoint binutils

RUN mkdir /var/run/sshd
RUN echo 'root:tutorial' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# ------------------------------------------------------------
# Add an 'tutorial' user
# ------------------------------------------------------------

RUN adduser --disabled-password --gecos "" tutorial && \
    echo "tutorial ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
ENV HOME /home/tutorial

# ------------------------------------------------------------
# Set-Up SSH with our Github deploy key
# ------------------------------------------------------------

RUN mkdir /home/tutorial/.ssh/
ADD ssh/config /home/tutorial/.ssh/config
ADD ssh/id_rsa.mpi /home/tutorial/.ssh/id_rsa
ADD ssh/id_rsa.mpi.pub /home/tutorial/.ssh/id_rsa.pub
ADD ssh/id_rsa.mpi.pub /home/tutorial/.ssh/authorized_keys

RUN chmod -R 600 /home/tutorial/.ssh/* && \
    chown -R tutorial:tutorial /home/tutorial/.ssh

# ------------------------------------------------------------
# Copy Rosa's MPI4PY example scripts
# ------------------------------------------------------------

ADD mpi4py_benchmarks /home/tutorial/mpi4py_benchmarks
RUN chown tutorial:tutorial /home/tutorial/mpi4py_benchmarks

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]


#-------------------------------------------------------------
# Install obspy
#-------------------------------------------------------------
RUN yes |  apt-get update
RUN yes |  apt-get install python
RUN yes |  apt-get install python-dev
RUN yes |  apt-get install python-setuptools
RUN yes |  apt-get install python-numpy
RUN yes |  apt-get install python-numpy-dev
RUN yes |  apt-get install python-scipy
RUN yes |  apt-get install python-matplotlib
RUN yes |  apt-get install python-lxml
RUN yes |  apt-get install python-sqlalchemy
RUN yes |  apt-get install python-suds
RUN yes |  apt-get install ipython

RUN pip install obspy

#---------------------------------------------------------------
# Install dispel4py
#---------------------------------------------------------------
RUN yes |  apt-get install zip
RUN yes |  apt-get install unzip
RUN yes |  apt-get install vim
RUN apt-get update && apt-get install wget curl python-dev python-pip python-setuptools git openmpi-bin openmpi-common libopenmpi-dev -y

# install dispel4py latest 
WORKDIR /home/tutorial
RUN git clone https://github.com/dispel4py/dispel4py.git
RUN cd dispel4py && python setup.py install

ADD tc_cross_correlation /home/tutorial/dispel4py/tc_cross_correlation
RUN chown tutorial:tutorial -R /home/tutorial/dispel4py/tc_cross_correlation
ADD command-preprocess.sh  /home/tutorial/.
ADD command-postprocess.sh  /home/tutorial/.
RUN chmod +x /home/tutorial/command-preprocess.sh  
RUN chown tutorial:tutorial /home/tutorial/command-preprocess.sh
RUN chmod +x /home/tutorial/command-postprocess.sh  
RUN chown tutorial:tutorial /home/tutorial/command-postprocess.sh
#---------------------------------------------------------------
#LD_LIBRARY_PATH
#---------------------------------------------------------------

RUN export LD_LIBRARY_PATH=/usr/lib/openmpi/lib/
