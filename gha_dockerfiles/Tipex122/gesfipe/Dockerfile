# start from an official image
FROM python:3.5

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/gesfipe_app/src
# RUN mkdir -p /opt/services/gesfipe_app/src/logs
# RUN touch /opt/services/gesfipe_app/src/logs/gesfipe.log
WORKDIR /opt/services/gesfipe_app/src

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
#XLH COPY Pipfile Pipfile.lock /opt/services/gesfipe_app/src/
#XLH RUN pip install pipenv && pipenv install --system



# install our two dependencies
# RUN pip install gunicorn django

# copy our project code
COPY . /opt/services/gesfipe_app/src
# WORKDIR /opt/services/gesfipe_app/src/gesfipe/

# RUN cd /opt/services/gesfipe_app/src/gesfipe/
RUN pip install pipenv && pipenv install --system

# expose the port 4000
EXPOSE 4000

# define the default command to run when starting the container
# CMD ["gunicorn", "--chdir", "gesfipe", "--bind", ":4000", "config.wsgi:application"]
CMD ["gunicorn", "--bind", ":4000", "config.wsgi:application"]

