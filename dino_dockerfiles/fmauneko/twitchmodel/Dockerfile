FROM mono:4.2

RUN mkdir -p /usr/src/app/source /usr/src/app/build
WORKDIR /usr/src/app/source

COPY . /usr/src/app/source
RUN curl -o./.nuget/NuGet.exe https://api.nuget.org/downloads/nuget.exe && chmod a+x ./.nuget/NuGet.exe
RUN xbuild /property:Configuration=ReleaseWithoutDocs /property:OutDir=/usr/src/app/build/
WORKDIR /usr/src/app/build

CMD [ "mono",  "./TwitchModel.exe" ]
