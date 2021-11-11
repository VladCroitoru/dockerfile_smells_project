FROM debian:latest

LABEL maintainer="Fabian Eulitz"

# Environment configuration
ENV CURA_APP_DIR=/srv/cura
ENV CURA_VERSION=4.11
ENV CURA_ENGINE_SEARCH_PATH=${CURA_APP_DIR}/definitions,${CURA_APP_DIR}/extruders

# Install required packages
RUN apt update -y && \
    apt install -y git autogen autoconf libtool build-essential cmake python3-dev python3-sip-dev protobuf-compiler libprotoc-dev libprotobuf-dev

# Install libArcus
WORKDIR ${CURA_APP_DIR}
RUN git clone --depth 1 https://github.com/Ultimaker/libArcus.git
WORKDIR ${CURA_APP_DIR}/libArcus/build
RUN cmake .. && make && make install
RUN rm -rf ${CURA_APP_DIR}/libArcus

# Install Cura Engine
WORKDIR ${CURA_APP_DIR}
RUN git clone -b ${CURA_VERSION} --depth 1 https://github.com/Ultimaker/CuraEngine.git
WORKDIR ${CURA_APP_DIR}/CuraEngine/build
RUN cmake .. && make && make install

# Make Cura ressources available for Cura Engine
WORKDIR ${CURA_APP_DIR}
RUN git clone -b ${CURA_VERSION} --depth 1 https://github.com/Ultimaker/Cura.git
RUN mv ${CURA_APP_DIR}/Cura/resources/definitions ${CURA_APP_DIR}/definitions && \
    mv ${CURA_APP_DIR}/Cura/resources/extruders ${CURA_APP_DIR}/extruders
RUN rm -r ${CURA_APP_DIR}/Cura

# Set CuraEngine as entrypoint
WORKDIR ${CURA_APP_DIR}
ENTRYPOINT [ "./CuraEngine/build/CuraEngine" ]




