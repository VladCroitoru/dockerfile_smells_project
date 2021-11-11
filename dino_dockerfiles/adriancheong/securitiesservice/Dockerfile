FROM microsoft/dotnet:latest
ENV name SecuritiesService
ENV buildconfig Release
COPY src/$name /root/$name
RUN cd /root/$name && dotnet restore && dotnet build -c $buildconfig && dotnet publish -c $buildconfig
RUN cp -rf /root/$name/bin/$buildconfig/netcoreapp1.0/publish/* /root/
EXPOSE 16555/tcp
ENTRYPOINT dotnet /root/${name}.dll
