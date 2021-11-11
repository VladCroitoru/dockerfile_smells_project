FROM virtualwatershed/vw-py


# Start installation with some necessary packages
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential \
    git wget curl unzip m4 openssh-client libncurses5-dev
RUN apt-get install -y libpq-dev libssl-dev libffi-dev

# install nodejs
RUN curl -sL https://deb.nodesource.com/setup_4.x | sh -
RUN apt-get install -y nodejs
RUN npm install -g bower


COPY . /var/www/prms-veg
WORKDIR /var/www/prms-veg
RUN NETCDF4_DIR=/usr/local && HDF5_DIR=/usr/local && pip install -r requirements.txt
ENV PYTHONPATH /var/www/prms-veg

RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN bower install
RUN git checkout -- app/static/bower_components/swagger-ui/dist/index.html

ENV APP_USERNAME abc@xyz.com
ENV APP_PORT 5000
ENV APP_PASSWORD prms

#CMD gunicorn --worker-class eventlet -w 4 manage:app -b 0.0.0.0:${APP_PORT} \
# --error-logfile='err.log' --access-logfile='log.log' --log-level DEBUG -e \
# APP_USERNAME=${APP_USERNAME} -e APP_PASSWORD=${APP_PASSWORD}

CMD python manage.py runserver -h 0.0.0.0 -p ${APP_PORT} --threaded

#CMD ./serve-swag.sh
