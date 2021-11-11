FROM ubuntu:16.10

RUN apt update && apt install curl libicu57 libunwind8 libcurl4-openssl-dev -y \
 && mkdir /opt/dotnet \
 && mkdir /opt/dotnet/1.1 \
 && cd /opt/dotnet/1.1 \
 && curl https://download.microsoft.com/download/E/7/8/E782433E-7737-4E6C-BFBF-290A0A81C3D7/dotnet-dev-ubuntu.16.10-x64.1.0.4.tar.gz -o 1.0.4.tar.gz \
 && tar -xvf *.tar.gz \
 && mkdir ../2.0 \
 && cd ../2.0 \
 && curl https://download.microsoft.com/download/1/B/4/1B4DE605-8378-47A5-B01B-2C79D6C55519/dotnet-sdk-2.0.0-linux-x64.tar.gz -o 2.0.tar.gz \
 && tar -xvf *.tar.gz 

RUN mkdir warmup \
    && cd warmup \
    && PATH=/opt/dotnet/1.1:$PATH dotnet new \
    && cd .. \
    && rm -rf warmup \
    && rm -rf /tmp/NuGetScratch

RUN mkdir warmup \
    && cd warmup \
    && PATH=/opt/dotnet/2.0:$PATH dotnet new \
    && cd .. \
    && rm -rf warmup \
    && rm -rf /tmp/NuGetScratch

CMD /container-prep.sh
