FROM buuck/clhep:2.3.4.4
MAINTAINER Micah Buuck (mbuuck@uw.edu)
WORKDIR /

#Install dependencies
RUN apt-get update && apt-get install -y cmake g++ gcc libexpat1-dev \
libxerces-c-dev libx11-dev libxmu-dev libgl1-mesa-dev

#Build geant4
RUN mkdir mjsw/mjdeps/geant4
WORKDIR mjsw/mjdeps/geant4
RUN mkdir src && mkdir build && mkdir install
COPY . src
WORKDIR build
RUN cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_INSTALL_PREFIX=../install -DCMAKE_BUILD_TYPE=RelWithDebInfo -DGEANT4_INSTALL_DATA=ON -DCLHEP_ROOT_DIR=$CLHEP_BASE_DIR -DCMAKE_COMPILER_IS_GNUCXX=ON -DGEANT4_USE_OPENGL_X11=ON -DGEANT4_USE_RAYTRACER_X11=ON -DGEANT4_USE_GDML=ON ../src 2>&1 | tee cmake.log
RUN make
RUN make install

WORKDIR /
CMD /bin/bash
