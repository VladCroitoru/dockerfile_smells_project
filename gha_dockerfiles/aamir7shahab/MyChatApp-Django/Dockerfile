# start from an official image
FROM python:3.6

# create and set working directory
RUN mkdir -p /opt/MyChatApp-Django
WORKDIR /opt/MyChatApp-Django

# copy the project
COPY . /opt/MyChatApp-Django

# install dependencies
RUN pip3 install -r /opt/MyChatApp-Django/requirements.txt

# collect static file 
RUN python fundoo/manage.py collectstatic --no-input

# to make it persisent
# VOLUME ['static_volume:/opt/MyChatApp-Django/fundoo/static']

# RUN python /opt/MyChatApp-Django/fundoo/manage.py collectstatic --noinput

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "fundoo", "--bind", ":8000", "fundoo.wsgi:application"]

