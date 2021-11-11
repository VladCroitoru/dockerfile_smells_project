FROM debian:stretch

RUN apt-get update -qq && apt-get install -yy git pandoc cmake qt5-default libnetpbm10-dev libhdf5-dev libfftw3-dev python-dev libhdf4-dev  g++ build-essential libtiff5-dev libgsl-dev qtmultimedia5-dev qttools5-dev libqt5svg5-dev libqt5scripttools5 qtscript5-dev libqt5multimediawidgets5 qttools5-dev-tools lsb-release libcfitsio-dev libhdf4-dev libhdf5-dev libhdf5-100 python-numpy

RUN git clone --recursive https://github.com/NeutrinoToolkit/Neutrino.git
RUN cd Neutrino/PythonQt && mkdir Linux && cd Linux && cmake -UQT_QMAKE_EXECUTABLE -DPythonQt_Wrap_QtAll=TRUE -DQt5_DIR=/usr/lib/x86_64-linux-gnu/cmake .. && make -j$(nproc) install && cd ../..
RUN cd Neutrino && mkdir Linux && cd Linux && cmake .. && make -j$(nproc) package
