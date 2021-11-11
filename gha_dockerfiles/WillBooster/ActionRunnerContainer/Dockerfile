FROM ubuntu
LABEL maintainer "Kazunori Sakamoto <exkazuu@willbooster.com>"

RUN apt-get update && apt-get upgrade -y
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata
RUN apt-get install -y git curl wget php build-essential make
RUN { curl -fsSL https://deb.nodesource.com/setup_16.x | bash -; }
RUN apt-get install -y nodejs
RUN npm install -g npm yarn
RUN npx playwright install-deps
RUN useradd --create-home --shell /bin/bash ci
RUN apt-get autoremove -y
RUN apt-get clean

USER ci
WORKDIR /home/ci
