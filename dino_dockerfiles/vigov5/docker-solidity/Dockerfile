FROM ubuntu:rolling

LABEL maintainer "Nguyen Anh Tien <nguyen.anh.tien@com> - Tran Duc Thang <tran.duc.thang@com>"

SHELL ["/bin/bash", "-c"]
RUN apt-get update
RUN apt-get install -y wget unzip python-virtualenv git build-essential software-properties-common curl
RUN add-apt-repository -y ppa:ethereum/ethereum-dev
RUN add-apt-repository -y ppa:ethereum/ethereum
RUN apt-get update
RUN apt-cache madison solc
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get install -y build-essential solc=1:0.4.23-0ubuntu1* ethereum python3 python-pip pandoc python3-pip \
    libssl-dev libcurl4-openssl-dev libffi-dev nodejs npm
RUN apt-get clean
RUN pip3 install requests web3 mythril
RUN wget -O /oyente.zip https://github.com/melonproject/oyente/archive/8ea5257e1e1f80dd2adde455817fbcfe179ee012.zip
RUN unzip /oyente.zip
RUN mv /oyente-8ea5257e1e1f80dd2adde455817fbcfe179ee012 /oyente
RUN npm install npm@latest -g  && npm install n --global && n stable
RUN npm install -g truffle@4.1.7 solium
RUN wget -O /usr/bin/framgia-ci https://raw.githubusercontent.com/framgia/ci-report-tool/master/dist/framgia-ci && chmod +x /usr/bin/framgia-ci
