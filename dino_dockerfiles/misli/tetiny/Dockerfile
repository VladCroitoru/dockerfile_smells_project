ARG CMS_TAG=latest
FROM misli/django-cms-site:$CMS_TAG

MAINTAINER Jakub Dorňák <jakub.dornak@misli.com>

# install other dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy files
COPY tetiny /app/tetiny

ENV SITE_MODULE=tetiny

# run this command at the end of any dockerfile based on this one
RUN django-cms collectstatic --no-input
