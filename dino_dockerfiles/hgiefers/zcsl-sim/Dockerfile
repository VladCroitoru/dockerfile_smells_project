FROM nimbix/centos-desktop
RUN yum -y update
RUN yum -y groupinstall "Development tools"
RUN yum -y install gperf gnuplot

RUN cd ; git clone https://github.com/steveicarus/iverilog.git ; cd iverilog ; git checkout --track -b v10-branch origin/v10-branch ; git pull
RUN cd ; cd iverilog ; sh autoconf.sh ;./configure ; make ; make install

RUN cd ; git clone https://github.com/hgiefers/zcsl.git
RUN cd ; cd zcsl/sw ; export VPI_USER_H_DIR=/usr/local/include/iverilog ; ./make-dep.sh 
RUN cd ; cd zcsl ; mkdir sim ; cd sim ; mkdir zcsl
RUN cd ; cd zcsl/sim/zcsl ; iverilog -o zcsl_isim ../../sw/pslse/afu_driver/verilog/top.v ../../hdl/zcsl/*.v ../../hdl/3rd_party/spiral-dft.v
RUN cd ; cd zcsl/sw/zcsl-fft ; sh ./run.sh
