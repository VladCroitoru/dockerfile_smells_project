# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from phusion/baseimage

maintainer cptfinch

run apt-get update

run apt-get install -y build-essential git
run apt-get install -y python python-dev python-setuptools
run apt-get install -y nginx supervisor
run apt-get install -y libatlas-dev libatlas-base-dev liblapack-dev
run apt-get install -y libpng12-dev libfreetype6 libfreetype6-dev
run apt-get install -y sqlite3

#scipy stack
run apt-get install -y python-numpy 
run apt-get install -y python-scipy 
run apt-get install -y python-matplotlib

run easy_install pip
run pip install uwsgi

# install our code
add . /home/docker/code/

# setup all the configfiles
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /home/docker/code/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /home/docker/code/supervisor-app.conf /etc/supervisor/conf.d/

# run pip install
run pip install -r /home/docker/code/requirements.txt

# clone qatrack+ to the app directory
run git clone https://cptfinch@bitbucket.org/cptfinch/qatrackplus.git /home/docker/code/app/.


#run cd /home/docker/code/app && mkdir db && python manage.py syncdb
#run python manage.py dumpdata --indent=2 auth > initial_data.json
#run python manage.py dumpdata --indent=2 sessions
#run python manage.py syncdb --noinput

# install django, normally you would remove this step because your project would already
# be installed in the code/app/ directory
# run django-admin.py startproject website /home/docker/code/app/ 

#expose 8000
#cmd ["supervisord", "-n"]
