FROM ubuntu:xenial

# install mono
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee /etc/apt/sources.list.d/mono-xamarin.list
RUN apt-get update && apt-get install -y mono-devel

# install paket 
RUN apt-get install -y nuget
RUN nuget install Paket -excludeversion -outputdirectory /opt/

# build XlsxValidator
RUN mkdir -p /app/xlsx-validator
ADD paket.dependencies /app/xlsx-validator
WORKDIR /app/xlsx-validator
RUN mono /opt/Paket/tools/paket.exe install
ADD . /app/xlsx-validator 
RUN xbuild /p:Configuration=Release

# generate xlxs-validator convenience script
RUN echo '#!/bin/sh' > /usr/local/bin/xlsx-validator && \ 
  echo 'mono /app/xlsx-validator/XlsxValidator/bin/Release/XlsxValidator.exe $@' >> /usr/local/bin/xlsx-validator && \
  chmod +x /usr/local/bin/xlsx-validator
