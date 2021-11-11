FROM gcc:9 AS sysroot
RUN curl -sS https://setup.inaccel.com/repository | sh \
 && apt install coral-api
WORKDIR /src/vadd
COPY src .
RUN g++ -std=c++17 vadd.cpp -lcoral-api -pthread

FROM inaccel/mkrt AS mkrt

ENV MKRT_SYSROOT_DIR=/host
ENV MKRT_CONFIG_PATH=/src

ENV MKRT_TOP_BUILD_DIR=/tmp

RUN --mount=from=sysroot,target=/host,ro mkrt

FROM scratch
COPY --from=mkrt /tmp /
ENTRYPOINT ["vadd/ld.so", "vadd/lib.so"]
