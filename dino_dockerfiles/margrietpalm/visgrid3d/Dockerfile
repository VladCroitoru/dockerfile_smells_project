FROM margrietpalm/visgrid3d-build

WORKDIR /src
COPY . /src/VisGrid3D

# build VisGrid3D
RUN mkdir -p VisGrid3D/build/
RUN cd VisGrid3D/build/ && cmake ../ && make

WORKDIR /app
RUN mv /src/VisGrid3D/build/VisGrid3D /app/VisGrid3D
RUN rm -rf /src

ENTRYPOINT ["/app/VisGrid3D"]
