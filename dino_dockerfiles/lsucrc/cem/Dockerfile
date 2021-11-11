FROM lsucrc/crcbase
USER crcuser
WORKDIR /model

# download the source code
RUN git clone https://github.com/csdms/cem-old
WORKDIR cem-old
RUN mkdir build
WORKDIR build
RUN cmake ../
RUN make 
ENV PATH $PATH:/model/cem-old/build



