FROM virtualwatershed/vw-py
MAINTAINER Moinul Hossain

LABEL description="This Image builds an ubuntu 14.04 image from vw-py:1.0 and installs the dependencies of vwadaptor." \
      version="1.0"

RUN apt-get update -y
RUN apt-get install -y libpq-dev
#set the env vars

# production or dev?
ENV VWADAPTOR_ENV dev
ENV VWADAPTOR_HOST 0.0.0.0
ENV VWADAPTOR_PORT 5000

# db uri
ENV VWADAPTOR_SQLALCHEMY_DATABASE_URI 'sqlite:////vwadaptor.db'
ENV VWADAPTOR_USER_DATABASE_URI 'sqlite:////vwauth.db'
# celery worker
ENV VWADAPTOR_CELERY_BROKER_URL redis://redis:6379/0
ENV VWADAPTOR_CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

# storage
ENV VWADAPTOR_STORAGE_PROVIDER LOCAL
ENV VWADAPTOR_STORAGE_KEY ''
ENV VWADAPTOR_STORAGE_SECRET ''
# container name or absolutepath for LOCAL storage
ENV VWADAPTOR_STORAGE_CONTAINER /vwstorage
ENV VWADAPTOR_STORAGE_SERVER true
ENV VWADAPTOR_STORAGE_SERVER_URL /download
ENV VWADAPTOR_STORAGE_EXTENSIONS nc,control
# for local create the directory to keep the files
RUN mkdir -p ${VWADAPTOR_STORAGE_CONTAINER}


# copy source code
COPY . /var/www/vwadaptor
WORKDIR /var/www/vwadaptor

# install requirements
#RUN echo bakkas
RUN pip install -r requirements/dev.txt
#
# expose the app port
EXPOSE ${VWADAPTOR_PORT}

# run the app server
#ENTRYPOINT ["python"]
#CMD ["manage.py","runserver","-p","${VWADAPTOR_PORT}","-h","${VWADAPTOR_HOST}"]
CMD python manage.py runserver -p ${VWADAPTOR_PORT} -h ${VWADAPTOR_HOST}
