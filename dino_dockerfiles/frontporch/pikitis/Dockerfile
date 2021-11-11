FROM openjdk:8-jdk
ENV OUTPUT_DIR=/opt/pikitis
ENV BUILD_FOLDER=/tmp/pikitis-build

# see README.md for other environment variables
ENV KAFKA_BROKERS="192.168.33.11:9092"

COPY . ${BUILD_FOLDER}

RUN cd ${BUILD_FOLDER} && \
    # install git, needed for our gradle build
    apt-get update > /dev/null && apt-get install -qq git && \

    # build with gradle
    ./gradlew assembleDist && \

    # unpack tar file
    chmod +x ./prepare-dist-tar && ./prepare-dist-tar && \

    # Create working dir
    mkdir -p ${OUTPUT_DIR} && \

    # Move the release folder contents up
    mv ./build/distributions/pikitis/* ${OUTPUT_DIR} && \

    # Change to pikitis directory
    cd ${OUTPUT_DIR} && \

    # Clean up after ourselves
    apt-get clean && rm -fr /tmp/*

WORKDIR ${OUTPUT_DIR}

CMD ["bin/kafka-transform-decrypt"]
