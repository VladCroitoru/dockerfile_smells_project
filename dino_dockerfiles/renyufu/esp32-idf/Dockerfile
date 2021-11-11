FROM ubuntu
RUN apt-get update
RUN apt-get install -y git wget make libncurses-dev flex bison gperf python python-serial
RUN mkdir /esp
WORKDIR /esp
RUN wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz
RUN tar -xzf xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz && rm -f xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz
ENV PATH=$PATH:/esp/xtensa-esp32-elf/bin
RUN git clone --recursive https://github.com/espressif/esp-idf.git
ENV IDF_PATH=/esp/esp-idf
VOLUME /proj
WORKDIR /proj
ENTRYPOINT ["make"]
