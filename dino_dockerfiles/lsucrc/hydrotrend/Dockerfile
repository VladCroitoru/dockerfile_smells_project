FROM lsucrc/crcbase
USER crcuser
WORKDIR /model

# download the source code
RUN git clone https://github.com/kettner/hydrotrend.git
WORKDIR hydrotrend
RUN mkdir build 
WORKDIR build
RUN cmake ./..
RUN make
ENV PATH $PATH:/model/hydrotrend/build
RUN chmod +rx /model/hydrotrend/build/run_hydrotrend

# running a testing case
WORKDIR ../data
RUN cp -r input/ HYDRO_IN
RUN mkdir HYDRO_OUTPUT
RUN run_hydrotrend -V
RUN diff HYDRO_OUTPUT/HYDROASCII.Q output/HYDROASCII.Q
