FROM microsoft/dotnet:1.1.4-runtime AS build-env 
RUN apt-get update && apt-get -y install apt-utils gcc make flex bison byacc git wget && git clone https://github.com/TonyAbell/tpc-ds.git && cd /tpc-ds/tools/ && make && wget -O ~/azcopy.tar.gz https://aka.ms/downloadazcopyprlinux

FROM microsoft/dotnet:1.1.4-runtime
COPY --from=build-env /root/azcopy.tar.gz /root
RUN tar -xf ~/azcopy.tar.gz -C ~/ && ~/install.sh && mkdir /tpc && rm -r ~/azcopy/ && rm ~/azcopy.tar.gz
COPY --from=build-env /tpc-ds/tools/tpcds.idx /tpc
COPY --from=build-env /tpc-ds/tools/dsdgen /tpc

COPY run.sh . 



