# add a base image
FROM lsucrc/crcbase
USER crcuser

# download swan source code and extract it 
WORKDIR /model
RUN wget http://swanmodel.sourceforge.net/download/zip/swan4120.tar.gz && \
    tar -zxvf swan4120.tar.gz 

# compile swan 
WORKDIR swan4120
RUN make config && make mpi

# set up enviroment variable of swan
ENV PATH $PATH:/model/swan4120
RUN chmod +rx /model/swan4120/swanrun 

# download test data and extract it 
WORKDIR /model
RUN wget http://swanmodel.sourceforge.net/download/zip/refrac.tar.gz && \
    tar -zxvf refrac.tar.gz

# test
WORKDIR /model/refrac
# RUN time swanrun -input a11refr -mpi 4
RUN echo 'swanrun -input a11refr -mpi 6' > /model/refrac/run.sh
RUN chmod 744 run.sh
