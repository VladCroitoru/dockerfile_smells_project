FROM alpine:edge
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk --update-cache add openssh-client python curl git rsync &&\
    curl -O -sSL https://bootstrap.pypa.io/get-pip.py &&\
    chmod +x ./get-pip.py && ./get-pip.py &&\
	rm -rf /var/cache/apk/*

COPY requirements.txt /usr/src/drone_composer/

RUN pip install --upgrade -r /usr/src/drone_composer/requirements.txt

COPY drone_composer/ /usr/src/drone_composer

RUN ln -s /usr/src/drone_composer/composer.py /usr/sbin/composer &&\
    ln -s /usr/src/drone_composer/snapshot.py /usr/sbin/snapshot

ENTRYPOINT ["/usr/sbin/composer"]
