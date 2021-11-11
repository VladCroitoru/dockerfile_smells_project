#
# Copyright 2017 Barracks Solution Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM ubuntu:16.04

MAINTAINER Simon Guerout <simon@barracks.io>

ENV SDK_ROOT=/opt/nordic

RUN apt-get update \
    && apt-get install -y lib32ncurses5 lib32z1 \
    && apt-get install -y gcc-arm-none-eabi \
    && apt-get install -y gdb-arm-none-eabi \
    && apt-get install -y build-essential \
    && apt-get install -y unzip \
		&& apt-get install -y wget

RUN mkdir -p /opt/nordic \
		&& wget https://developer.nordicsemi.com/nRF5_SDK/nRF5_SDK_v12.x.x/nRF5_SDK_12.2.0_f012efa.zip -O nordic_sdk.zip \
		&& unzip nordic_sdk.zip 'components/*' 'external/*' 'svd/*' -d $SDK_ROOT \
		&& rm nordic_sdk.zip

COPY Makefile.posix $SDK_ROOT/components/toolchain/gcc/Makefile.posix
