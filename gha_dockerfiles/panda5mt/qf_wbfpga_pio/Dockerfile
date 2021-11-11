FROM debian:buster-slim 
RUN apt update && apt -y install --no-install-recommends sudo make libtbb2 wget coreutils udev curl time tar\
    && apt -y install git gcc-arm-none-eabi\
    && apt clean && rm -rf /var/lib/apt/lists/*

RUN git clone -b v1.10.0 https://github.com/QuickLogic-Corp/qorc-sdk.git
SHELL ["/bin/bash", "-c"]
WORKDIR /qorc-sdk 
RUN mkdir -p arm_toolchain_install/gcc-arm-none-eabi-9-2020-q2-update/
RUN ln -s /usr/bin/ arm_toolchain_install/gcc-arm-none-eabi-9-2020-q2-update/
#RUN sed -i -e 's/v1.3.1/v1.3.2/g' envsetup.sh 
#RUN source envsetup.sh
WORKDIR /root
RUN echo -e '#!/bin/bash\n\ncd /qorc-sdk\nsource envsetup.sh\ncd -\nmake all -C GCC_Project\n# scp GCC_Project/output/bin/*.bin pi@raspberrypi.local:/home/pi\n' > qlogic_build.sh 
#RUN echo -e '#!/bin/bash\nqfprog="python3 /qorc-sdk/TinyFPGA-Programmer-Application/tinyfpga-programmer-gui.py"\n$qfprog --port /dev/ttyUSB0  --m4app GCC_Project/output/bin/*.bin --mode fpga-m4' > qlogic_write.sh
RUN sed -i 's/\r//' *.sh
RUN chmod +x qlogic_build.sh
RUN chmod +x add_git.sh
WORKDIR /qorc-sdk/qf_apps
#avoid cache
ARG CACHEBUST=1
RUN git clone https://github.com/panda5mt/qf_wbfpga_pio.git