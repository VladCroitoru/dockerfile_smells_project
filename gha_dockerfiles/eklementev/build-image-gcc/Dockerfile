from ubuntu:20.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
      git make cmake gcc g++ libssl-dev qtbase5-dev qtbase5-private-dev qtdeclarative5-dev libqt5svg5-dev qttools5-dev qtmultimedia5-dev

