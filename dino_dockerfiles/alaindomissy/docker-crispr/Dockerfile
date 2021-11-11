FROM alaindomissy/docker-biopython
MAINTAINER Alain Domissy alaindomissy@gmail.com

RUN conda install -y \
  cycler==0.9.0 \
  cython==0.23.4 \
  decorator==4.0.6 \
  py==1.4.31 \
  pyparsing==2.0.3 \
  matplotlib==1.5.1 \
  pyqt==4.11.4

# already there
#  python-dateutil==2.4.2 \
#  pytz==2015.7
#  numpy==1.10.4 \

# ubunutu distro backup
RUN apt-get install -y duply

COPY files /
RUN chmod 600 /root/.ssh/id_rsa && \
    ln -s /RESTORE /BLASTDB && \
    ln -s /RESTORE /PROTOSP

#    && \
#    ln -s /data/dev /root/pycrispr


# /root/.cache/duplicity was already COPYed , but this makes an update
# RUN duply mm8 status && duply hg18 status && duply ecoli status && duply phix status
# ABOVE DOES NOT WORK DUE TO ssh key not protected with 600 permissions somehow


# RUN apt-get install nano


# virtual envs    NOT NEEDED
###############
# RUN conda create -q -n crisprenv
# how to source activate in a Dockerfile? dont know, for now no venv
# source activate root


# RUN git clone https://github.com/alaindomissy/pycrispr.git
# RUN pip install /root/pycrispr/

# RUN pip install git+https://github.com/alaindomissy/pycrispr.git

# root development executables
# app executables
ENV PATH /opt/blast/bin:/root/bin:/BACKEND:$PATH

WORKDIR /root/

RUN apt-get install nano tree

CMD /BACKEND/appgithub.sh
