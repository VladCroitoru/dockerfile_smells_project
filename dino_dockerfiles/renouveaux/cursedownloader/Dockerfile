FROM python:alpine3.6

MAINTAINER <Renouveaux>

RUN apk update && apk upgrade && apk add git
WORKDIR /tmp

RUN git clone https://github.com/portablejim/curseDownloader.git .

RUN pip3 install -r requirements.txt

RUN cp downloader.py /usr/bin/downloader.py
RUN cp updater.py /usr/bin/updater.py

RUN mkdir /pack

VOLUME ["/pack"]
WORKDIR /pack

CMD "python" "/usr/bin/downloader.py" "--manifest" "manifest.json" "--nogui"
