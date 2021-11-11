# Copyright © (C) 2017 Emory Merryman <emory.merryman@gmail.com>
#   This file is part of whitebackpack.
#
#   whitebackpack is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   whitebackpack is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with whitebackpack.  If not, see <http://www.gnu.org/licenses/>.
FROM tidyrailroad/base:0.2.3
MAINTAINER Emory Merryman <emory.merryman@gmail.com>
COPY run.sh entrypoint.sh /opt/docker/
RUN ["/bin/sh", "/opt/docker/run.sh"]
ENTRYPOINT ["/bin/sh", "/opt/docker/entrypoint.sh"]
CMD []
