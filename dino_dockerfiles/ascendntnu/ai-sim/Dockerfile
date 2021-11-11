FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install libegl1-mesa-dev libgles2-mesa-dev libmirclient-dev libxkbcommon-dev libsdl2-dev -y

WORKDIR /srv/ai-sim
CMD ./COMPILE_AND_RUN_SIM.sh
