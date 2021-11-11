FROM node:10
RUN yarn global add elm --no-progress
RUN git clone https://github.com/obmarg/libsysconfcpus.git;
RUN cd libsysconfcpus && ./configure && make && make install && cd ../
