FROM theshadowx/qt5:latest as builder

RUN apt update && apt install -y cmake liblog4cplus-dev qttools5-dev libboost-dev libboost-test-dev libboost-python-dev

WORKDIR /workspace
COPY . .

RUN cmake .
RUN cmake --build . -- -j 4 #TODO determine number


FROM theshadowx/qt5:latest

RUN apt update && apt install -y cmake liblog4cplus-dev libboost-python-dev \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/
COPY --from=builder /workspace/logWitch logWitch

EXPOSE 9998
EXPOSE 9020

CMD logWitch/logwitch
