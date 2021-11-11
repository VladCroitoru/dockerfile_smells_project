FROM alpine AS builder

RUN apk add --update --no-cache \
    make cmake gcc g++ libstdc++ libgcc git zlib-dev \
    openssl-dev boost-dev curl-dev \
    postgresql-dev mariadb-dev \
    librdkafka-dev nlohmann-json

RUN git clone https://github.com/stephb9959/poco /poco
RUN git clone https://github.com/stephb9959/cppkafka /cppkafka
RUN git clone --recurse-submodules https://github.com/aws/aws-sdk-cpp /aws-sdk-cpp
RUN git clone https://github.com/pboettch/json-schema-validator /json-schema-validator

WORKDIR /aws-sdk-cpp
RUN mkdir cmake-build
WORKDIR cmake-build
RUN cmake .. -DBUILD_ONLY="s3" \
             -DCMAKE_BUILD_TYPE=Release \
             -DCMAKE_CXX_FLAGS="-Wno-error=stringop-overflow -Wno-error=uninitialized" \ 
             -DAUTORUN_UNIT_TESTS=OFF
RUN cmake --build . --config Release -j8
RUN cmake --build . --target install

WORKDIR /cppkafka
RUN mkdir cmake-build
WORKDIR cmake-build
RUN cmake ..
RUN cmake --build . --config Release -j8
RUN cmake --build . --target install

WORKDIR /poco
RUN mkdir cmake-build
WORKDIR cmake-build
RUN cmake ..
RUN cmake --build . --config Release -j8
RUN cmake --build . --target install

WORKDIR /json-schema-validator
RUN mkdir cmake-build
WORKDIR cmake-build
RUN cmake ..
RUN make
RUN make install

ADD CMakeLists.txt build /owprov/
ADD cmake /owprov/cmake
ADD src /owprov/src

WORKDIR /owprov
RUN mkdir cmake-build
WORKDIR /owprov/cmake-build
RUN cmake ..
RUN cmake --build . --config Release -j8

FROM alpine

ENV OWPROV_USER=owprov \
    OWPROV_ROOT=/owprov-data \
    OWPROV_CONFIG=/owprov-data

RUN addgroup -S "$OWPROV_USER" && \
    adduser -S -G "$OWPROV_USER" "$OWPROV_USER"

RUN mkdir /openwifi
RUN mkdir -p "$OWPROV_ROOT" "$OWPROV_CONFIG" && \
    chown "$OWPROV_USER": "$OWPROV_ROOT" "$OWPROV_CONFIG"
RUN apk add --update --no-cache librdkafka curl-dev mariadb-connector-c libpq su-exec gettext ca-certificates bash jq curl

COPY --from=builder /owprov/cmake-build/owprov /openwifi/owprov
COPY --from=builder /cppkafka/cmake-build/src/lib/* /lib/
COPY --from=builder /poco/cmake-build/lib/* /lib/
COPY --from=builder /aws-sdk-cpp/cmake-build/aws-cpp-sdk-core/libaws-cpp-sdk-core.so /lib/
COPY --from=builder /aws-sdk-cpp/cmake-build/aws-cpp-sdk-s3/libaws-cpp-sdk-s3.so /lib/

COPY owprov.properties.tmpl /
COPY docker-entrypoint.sh /
RUN wget https://raw.githubusercontent.com/Telecominfraproject/wlan-cloud-ucentral-deploy/main/docker-compose/certs/restapi-ca.pem \
    -O /usr/local/share/ca-certificates/restapi-ca-selfsigned.pem

COPY readiness_check /readiness_check

EXPOSE 16005 17005 16105

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/openwifi/owprov"]
