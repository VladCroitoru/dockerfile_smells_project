FROM kaskada/cmake-gcc5

RUN git clone https://github.com/jimporter/bencode.hpp.git && \
    make -C bencode.hpp install && \
    rm -r bencode.hpp

RUN git clone https://github.com/jimporter/mettle.git && \
    make -C mettle install && \
    rm -r mettle

