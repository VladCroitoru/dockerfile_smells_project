# vim:set sw=4 ts=4 et:
#
# weaver-builder: build Docker images from Weaverfiles.
#
# Copyright (c) 2015, 2016 Torchbox Ltd.
# Original author: Felicity Tarnell <felicity@torchbox.com>.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely. This software is provided 'as-is', without any express or implied
# warranty.
#

FROM python:3-alpine

RUN apk --no-cache add openssh-client git docker
RUN pip install pyyaml

COPY weaver /

CMD ["/weaver"]
