# Spiderbot: Web Validation Robot
# Copyright (C) 2015  Julio Martínez Martínez-Checa

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# Contact: julioxus@gmail.com

# University of Granada, hereby disclaims all copyright
# interest in the program `Spiderbot' written 
# by Julio Martínez Martínez-Checa.

# signature of Julio Martínez Martínez-Checa, 23 June 2015
# Julio Martínez Martínez-Checa, Student at the University of Granada.

FROM ubuntu:latest
MAINTAINER Julio Martínez Martínez-Checa <julioxus@gmail.com>

#Instalar Python con todas las dependencias

RUN apt-get update
RUN apt-get -y install python python-setuptools build-essential python-dev
RUN easy_install pip

# Instalamos git y clonamos el repositorio
RUN apt-get install -y git
RUN git clone https://github.com/julioxus/spiderbot.git

# Descargamos los submódulos que faltan, GAE en este caso
# e iniciamos la instalación de la aplicación que incluye 
# el demonio de la misma
RUN cd spiderbot && \
git submodule init && \
git submodule sync && \
git submodule update && \
chmod 755 install.sh && \
bash install.sh

# Iniciamos el servicio
RUN service spiderbot restart

# Exponemos puerto 80
EXPOSE 80