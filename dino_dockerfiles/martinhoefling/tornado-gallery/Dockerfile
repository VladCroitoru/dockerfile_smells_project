FROM ubuntu:trusty
MAINTAINER Martin Hoefling <martin.hoefling@gmx.de>

COPY .bowerrc bower.json requirements.txt setup.py /opt/tgallery/
COPY tgallery /opt/tgallery/tgallery

WORKDIR /opt/tgallery

RUN DEBIAN_FRONTEND="noninteractive" apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y nodejs npm python3 python3-pip python-virtualenv python3-dev build-essential zlib1g-dev libjpeg-dev libexempi3 git && \
    npm install -g bower && \
    ln -s /usr/bin/nodejs /usr/local/bin/node && \
    bower --allow-root install && \
    virtualenv -p python3  /opt/tgallery/venv && \
    /opt/tgallery/venv/bin/pip install -r requirements.txt && \
    /opt/tgallery/venv/bin/python setup.py develop && \
    DEBIAN_FRONTEND="noninteractive" apt-get remove --purge -y nodejs npm python3-pip python-virtualenv python3-dev build-essential && \
    DEBIAN_FRONTEND="noninteractive" apt-get autoremove --purge -y  && \
    DEBIAN_FRONTEND="noninteractive" apt-get clean  && \
    rm -rf /var/lib/apt/lists

VOLUME /gallery

ENTRYPOINT '/opt/tgallery/venv/bin/tgallery'
CMD ['--picture_path=/gallery']

