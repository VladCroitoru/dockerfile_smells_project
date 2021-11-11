# Copyright © 2017 by Jeffrey C. Ollie <jeff@ocjtech.us>
#
# This file is part of Nest Exporter.
#
# Nest Exporter is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Nest Exporter is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Nest Exporter.  If not, see
# <http://www.gnu.org/licenses/>.

FROM registry.fedoraproject.org/fedora:26

ENV LANG C.UTF-8

RUN dnf -y update --disablerepo=* --enablerepo=fedora --enablerepo=updates --enablerepo=updates-testing && \
    dnf -y install python3 python3-devel python3-virtualenv gcc redhat-rpm-config \
                   openssl-devel libffi-devel && \
    virtualenv-3 /opt/nest_exporter && \
    /opt/nest_exporter/bin/pip install --upgrade pip && \
    /opt/nest_exporter/bin/pip install --upgrade setuptools && \
    /opt/nest_exporter/bin/pip install --upgrade 'Twisted[tls]' \
                                                 'python-nest < 3.0' && \
    dnf -y remove python3-devel python3-virtualenv gcc redhat-rpm-config openssl-devel libffi-devel && \
    rm -rf /usr/share/doc/* /usr/share/man/* /var/cache/dnf/* /tmp/*

COPY setup.py /src/setup.py
COPY src /src/src

RUN cd /src && /opt/nest_exporter/bin/python setup.py install
RUN rm -rf /src

EXPOSE 9264

ENTRYPOINT ["/opt/nest_exporter/bin/nest_exporter"]
