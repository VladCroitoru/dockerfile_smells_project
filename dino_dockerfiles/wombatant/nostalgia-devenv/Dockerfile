FROM wombatant/devenv

ENV DEVKITPRO /opt/devkitPro
ENV DEVKITARM ${DEVKITPRO}/devkitARM

###############################################################################
# Install Ox

RUN git clone https://github.com/wombatant/ox.git /usr/local/src/ox && \
    cd /usr/local/src/ox && \
    git checkout -b install release-0.1; \
	 # setup build dirs
    mkdir -p \
             /usr/local/src/ox/build/release \
             /usr/local/src/ox/build/windows \
             /usr/local/src/ox/build/gba; \
    # install Ox for native environment
    cd /usr/local/src/ox/build/release && \
    cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON ../../ && \
    make -j install; \
    # install Ox for GBA
    cd /usr/local/src/ox/build/gba && \
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
          -DCMAKE_TOOLCHAIN_FILE=cmake/Modules/GBA.cmake \
          -DCMAKE_INSTALL_PREFIX=/opt/devkitPro/devkitARM \
          -DOX_USE_STDLIB=OFF ../../ && \
    make -j install; \
    # install Ox for Windows
    cd /usr/local/src/ox/build/windows && \
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
          -DCMAKE_TOOLCHAIN_FILE=cmake/Modules/Mingw.cmake \
          -DCMAKE_INSTALL_PREFIX=/usr/x86_64-w64-mingw32 \
          -DOX_BUILD_EXEC=OFF ../../ && \
    make -j install
