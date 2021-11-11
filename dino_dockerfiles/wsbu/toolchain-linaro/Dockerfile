FROM wsbu/toolchain-native:v0.3.10

ENV WSBU_C_COMPILER=arm-linux-gnueabihf-gcc \
  WSBU_CXX_COMPILER=arm-linux-gnueabihf-g++ \
  WSBU_EMULATOR=/usr/bin/qemu-arm \
  QEMU_LD_PREFIX=/usr/arm-linux-gnueabihf \
  CMAKE_TOOLCHAIN_FILE=/opt/toolchain-linaro-armhf.cmake

ENV CONAN_CMAKE_TOOLCHAIN_FILE="${CMAKE_TOOLCHAIN_FILE}" \
  CC="${WSBU_C_COMPILER}" \
  CXX="${WSBU_CXX_COMPILER}"

# Replace native-oritented build configurations
COPY toolchain.cmake "${CMAKE_TOOLCHAIN_FILE}"
COPY conan/sitara_profile "${HOME}/.conan/profiles/sitara"

RUN apt-get update && apt-get install --yes --no-install-recommends \
      qemu-system-arm \
      qemu-user \
      gcc-arm-linux-gnueabihf \
      g++-arm-linux-gnueabihf \
      gccgo-arm-linux-gnueabihf \
      libncurses5-dev \
      && rm --recursive --force /var/lib/apt/lists/* \
  && pip3 --no-cache-dir install python-magic \
  && mkdir --parents $HOME/.ssh \
  && ln -sf "${HOME}/.conan/profiles/sitara" "${HOME}/.conan/profiles/default" \
  && chown --recursive captain:captain "$HOME" \
  && chmod --recursive 777 "$HOME"

LABEL "net.redlion.controller.platform"="s5t"
