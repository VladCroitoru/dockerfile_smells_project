FROM d356/sh2-gcc-docker
ENV compiler=/carl9170fw/toolchain/inst/bin/sh-elf-gcc root_path=/carl9170fw/toolchain/inst/bin/ toolchain_file=/yabause/yabauseut/Platform/SegaSaturn
RUN git clone https://github.com/cyberwarriorx/iapetus.git

COPY yabause yabause

# compile iapetus
RUN cd iapetus ; \
    mkdir build ; \
    cd build ; \
    cmake .. -DCMAKE_TOOLCHAIN_FILE=${toolchain_file} -DCMAKE_C_COMPILER=${compiler} -DCMAKE_FIND_ROOT_PATH=${root_path} ; \
    make

#compile yabauseut
RUN cd yabause ; \ 
    mkdir yabauseut/build ; \
    cd yabauseut/build ; \
    cmake .. -DCMAKE_TOOLCHAIN_FILE=${toolchain_file} -DWANT_AUTOMATED_TESTING=ON -DCMAKE_C_COMPILER=${compiler}  -DCMAKE_FIND_ROOT_PATH=${root_path} -DIAPETUS_ROOT_PATH=/iapetus -DIAPETUS_INCLUDE_DIR=/iapetus/src -DIAPETUS_LIB=/iapetus/build/src/libiapetus.a ; \
    make

#compile yabause-runner
RUN cd yabause/yabause/src/runner ; \
    mkdir build ; \
    git clone git://github.com/lvandeve/lodepng.git ; \
    cd build ; \
    cmake -DYAB_PORTS=runner -DSH2_DYNAREC=OFF -DYAB_WANT_C68K=OFF -DYAB_WANT_Q68=OFF -DYAB_WANT_OPENGL=OFF ../../ ; \
    make 
    
#run tests
RUN cd /yabause/yabause/src/runner/build ; \ 
    git clone git://github.com/d356/yabauseut-bin.git ; \
    runner/yabause yabauseut check /yabause/yabauseut/build/src/YabauseUT.elf yabauseut-bin/vdp2_screenshots/ yabauseut-bin/vdp1_framebuffers/