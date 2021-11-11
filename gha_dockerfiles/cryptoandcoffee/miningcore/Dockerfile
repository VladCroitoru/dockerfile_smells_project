FROM ubuntu:18.04
COPY ./build.sh /
COPY ./config.json /
RUN ./build.sh
CMD dotnet /miningcore/build/Miningcore.dll -c /config.json
