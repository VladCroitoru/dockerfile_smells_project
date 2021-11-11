FROM vcatechnology/linux-mint

RUN apt-get update -qq && apt-get install -yy git pandoc cmake qt5-default libnetpbm10-dev libhdf5-dev libhdf5-10 libfftw3-dev python-dev libhdf4-dev g++ build-essential libtiff5-dev libgsl-dev qtmultimedia5-dev qttools5-dev libqt5svg5-dev libqt5multimediawidgets5 qttools5-dev-tools lsb-release libcfitsio-dev devscripts debhelper

RUN git clone https://github.com/iltommi/PythonQt.git
RUN cd PythonQt && git checkout mint && cmake -UQT_QMAKE_EXECUTABLE -DPythonQt_Wrap_QtAll=TRUE -DQt5_DIR=/usr/lib/x86_64-linux-gnu/cmake . && make -j$(nproc) install

RUN git clone https://github.com/NeutrinoToolkit/Neutrino.git
RUN cd Neutrino && mkdir Linux && cd Linux && cmake .. && make -j$(nproc) package && make install
