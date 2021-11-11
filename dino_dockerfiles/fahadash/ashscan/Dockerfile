FROM opensuse:tumbleweed

RUN mkdir /ashscan

COPY . /ashscan/

RUN zypper --non-interactive install mono-devel

# RUN sudo zypper install git

RUN zypper --non-interactive install wget

RUN /usr/bin/wget -P /ashscan/.nuget/ https://dist.nuget.org/win-x86-commandline/latest/nuget.exe
RUN /usr/bin/mv /ashscan/.nuget/nuget.exe /ashscan/.nuget/NuGet.exe

#RUN /usr/bin/xbuild /property:Configuration=Release /property:ReferencePath=/ashscan/release/ /property:WorkingDirectory=/ashscan /property:OutDir=/ashscan/release/ /ashscan/ashscan.sln

RUN cd /ashscan && xbuild /property:Configuration=Release /property:OutDir=./ashscan/ /property:DefineConstants="DOCKER" ashscan.sln

RUN touch /ashscan/release/data/Bannedhosts.txt
RUN touch /ashscan/release/data/Bannedwords.txt

RUN mkdir /ashscan/release/Data
RUN chmod u+x /ashscan/dockerstart.sh


