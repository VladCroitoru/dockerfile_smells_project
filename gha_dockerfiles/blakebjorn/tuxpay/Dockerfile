FROM ubuntu:21.04
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

RUN apt-get update \
    && apt-get install python3-pip libsecp256k1-dev npm wkhtmltopdf -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tuxpay
COPY requirements.txt requirements.txt
COPY modules/electrum_mods/Electron-Cash-4.2.4.tar.gz .
COPY modules/electrum_mods/electrum-4.1.2.tar.gz .
RUN pip3 install --no-cache-dir -r requirements.txt

RUN npm install -g npm@7.19.1

COPY sdk/package.json sdk/package.json
COPY sdk/package-lock.json sdk/package-lock.json
RUN cd sdk && npm install

COPY admin/package.json admin/package.json
COPY admin/package-lock.json admin/package-lock.json
RUN cd admin && npm install

COPY . .

RUN cd sdk && npm run build
RUN cd admin && npm run generate
CMD ['python3', 'server.py']