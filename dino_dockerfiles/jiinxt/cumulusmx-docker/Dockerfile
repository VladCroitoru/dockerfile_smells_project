FROM debian:wheezy
MAINTAINER Joey Stout <jstout@jiinxt.com>

ARG TZ=America/Indiana/Indianapolis

RUN apt-get update \
   && apt-get upgrade -y \
   && apt-get install -y wget unzip software-properties-common curl \
    && rm -rf /var/lib/apt/lists/*

RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF

RUN echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/4.0.5.1 main" > /etc/apt/sources.list.d/mono-xamarin.list \
        && apt-get update \
        && apt-get install -y mono-complete \
        && rm -rf /var/lib/apt/lists/*

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN wget https://s3.us-east-2.amazonaws.com/jiinxt.com/CumulusMX.zip
RUN unzip CumulusMX.zip

CMD cd CumulusMX && mono CumulusMX.exe