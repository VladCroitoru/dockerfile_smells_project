# Copyright (c) 2001-2017 Convertigo SA.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, see<http://www.gnu.org/licenses/>.

FROM openjdk:8

MAINTAINER Nicolas Albert nicolasa@convertigo.com

## Install git-lfs (https://github.com/git-lfs/git-lfs/wiki/Installation)

RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends\
    	git-lfs \
    	maven \
    && git lfs install && \
    rm -r /var/lib/apt/lists/*
