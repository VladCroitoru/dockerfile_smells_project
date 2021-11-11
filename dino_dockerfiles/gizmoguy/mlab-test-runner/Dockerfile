FROM ubuntu
MAINTAINER Peter Boothe <pboothe@google.com>
# Install the packages we need
RUN apt-get update && apt-get install -y git automake gcc make libssl-dev libjansson-dev python
RUN git clone --recursive https://github.com/ndt-project/ndt
RUN cd ndt/I2util && ./bootstrap.sh && ./configure && make && make install
RUN cd ndt && ./bootstrap && ./configure && make
ADD run_tests.py /run_tests.py
RUN chmod +x /run_tests.py
CMD /run_tests.py
