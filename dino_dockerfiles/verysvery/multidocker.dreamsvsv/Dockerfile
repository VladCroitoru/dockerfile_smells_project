##############################
######### CopyRights(c) 2015 VerysVery.com  #########
######### Released under the MIT License #########
######### http://opensource.org/licenses/mit-license.php #########
##############################

FROM python:latest

### Docker-Compose ###
### Binary Data ###
ENV PYTHONUNBUFFERED 1

######### boot2docker Setup #########
### Link Directory ###
RUN mkdir /DreamsVsV
WORKDIR /DreamsVsV
ADD . /DreamsVsV/

### Pip Setup ###
ADD requirements.txt /DreamsVsV/
RUN pip install -r requirements.txt --allow-all-external

### CMD Setup ###
# CMD docker-compose run dreamsvsv python manage.py startapp polls
# CMD docker-compose run dreamsvsv django-admin.py startproject DreamsVsV .
