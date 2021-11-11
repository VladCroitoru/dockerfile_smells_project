FROM ogrisel/openblas
MAINTAINER lhhung
RUN apt-get update && apt-get install -y libmpich-dev wget g++ nano
RUN wget https://sourceforge.net/projects/boost/files/boost/1.57.0/boost_1_57_0.tar.bz2/download
RUN tar -xjvf download
RUN rm download -rf
WORKDIR ./boost_1_57_0
RUN ["/bin/bash", "bootstrap.sh"]
RUN echo 'using mpi ;' >> project-config.jam
RUN ./b2 -j8 -target=shared,static; exit 0; 
RUN ./b2 install; exit 0;
COPY fastBMAMPI /usr/local/bin/fastBMA
WORKDIR /
RUN rm ./boost_1_57_0 -rf
RUN echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
RUN apt-get remove -y gcc g++ nano
