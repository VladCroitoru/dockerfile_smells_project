FROM stevenrbrandt/science-base
USER root
RUN apt-get update
RUN apt-get install -y curl
RUN mkdir /model
RUN mkdir /work
RUN mkdir /project
RUN mkdir /project/singularity
RUN mkdir /project/singularity/bin
RUN mkdir /var/spool/torque
RUN chown jovyan /var/spool/torque
RUN chown jovyan /project
RUN chown jovyan /project/singularity
RUN chown jovyan /project/singularity/bin
RUN chown jovyan /model
RUN chown jovyan /work
RUN touch /etc/ssh/ssh_known_hosts
USER jovyan

# download swan source code and extract it 
WORKDIR /model
COPY swan4120.tar.gz swan4120.tar.gz
RUN tar -zxvf swan4120.tar.gz
    
# compile swan 
WORKDIR swan4120
RUN make config && make mpi

# set up enviroment variable of swan
ENV PATH $PATH:/model/swan4120
RUN chmod +rx /model/swan4120/swanrun 

# download test data and extract it 
WORKDIR /model
COPY refrac.tar.gz refrac.tar.gz
RUN tar -zxvf refrac.tar.gz

# set up data directory for bind external data 
RUN mkdir data

# test
WORKDIR /model/refrac
# RUN time swanrun -input a11refr -mpi 4
RUN echo 'swanrun -input a11refr -mpi 6' > /model/refrac/run.sh
RUN chmod 744 run.sh
