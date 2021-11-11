FROM efifogel/sgal:latest-pre

RUN mkdir /usr/src/sgal
WORKDIR /usr/src/sgal
COPY ../../CMakeLists.txt ./
ADD ../../src ./src
ADD ../../cmake ./cmake

RUN cmake -DCMAKE_BUILD_TYPE=Release \
  	  -DBUILD_SHARED_LIBS=true \
          -DSGAL_USE_DXF:BOOL=ON \
          -DSGAL_USE_V8:BOOL=ON \
          -DSGAL_USE_SCGAL:BOOL=ON \
          -DSGAL_USE_POS:BOOL=OFF \
          -DSGAL_USE_VOS:BOOL=OFF \
          -DSGAL_USE_CGM:BOOL=OFF \
          -DSGAL_USE_LTS:BOOL=OFF \
          -DSGAL_USE_SGM:BOOL=OFF \
	  -DSGAL_USE_NGM:BOOL=OFF \
          -DSGAL_BUILD_PYBINDINGS:BOOL=ON \
          -DSGAL_TRACE:BOOL=ON .
RUN make install

# RUN apt-get install -y mesa-utils
