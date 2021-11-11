FROM debian:buster-slim

WORKDIR root

RUN apt-get update && \
	  apt-get install -y --no-install-recommends build-essential sudo ca-certificates git \
				    gcc-arm-none-eabi libstdc++-arm-none-eabi-newlib pkg-config libusb-1.0.0-dev cargo

RUN git clone --depth 1 https://github.com/OpenAnnePro/AnnePro2-Tools tools
RUN cd tools && cargo build --release

RUN git clone --depth 1 --recursive https://github.com/OpenAnnePro/qmk_firmware qmk
RUN git clone --depth 1 --recursive https://github.com/OpenAnnePro/AnnePro2-Shine shine

RUN mkdir /data
VOLUME /data

RUN mkdir /build
VOLUME /build

COPY build.sh .
