# This file is part of rawstorm.
#
#    rawstorm is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    rawstorm is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with rawstorm .  If not, see <http://www.gnu.org/licenses/>.
FROM fedora:25
COPY root /opt/docker/
RUN ["/usr/bin/sh", "/opt/docker/run.sh"]
ENTRYPOINT ["/usr/bin/sh", "/opt/docker/entrypoint.sh"]