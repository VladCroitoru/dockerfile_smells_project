# Start off a msis/ibex-env image based on wheezy
FROM msis/ibex-env

# Feel free to email me if you need support
MAINTAINER Mohamed Saad IBN SEDDIK <ms.ibnseddik@gmail.com>

WORKDIR /usr/src/cmake

COPY cmake-3.2.2.tar.gz /usr/src/cmake/

RUN tar xzvf cmake-3.2.2.tar.gz \
  && rm cmake-3.2.2.tar.gz \
  && cd cmake-3.2.2 \
  && ./bootstrap \
  && make -j$(nproc) \
  && make install

COPY Step4 /root/workspace/TutorialS4

WORKDIR /root/workspace/TutorialS4/build

RUN cmake .. \
  && make -j$(nproc) \
  && ctest Tutorial