FROM ubuntu:17.10

RUN buildDeps='g++ gcc libc6-dev make wget python python-argparse curl libmpc-dev libmpfr-dev libgmp-dev' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && wget https://raw.githubusercontent.com/oscourse-tsinghua/ucore_plus/master/ucore/misc/create_build_env.py \
    && python create_build_env.py --build_threads=8 --gcc_major_versions=4,5,6,7 /opt/ucore_build_environment \
    && rm -rf /opt/ucore_build_environment/gcc* \
    && rm -rf /opt/ucore_build_environment/binutils*
