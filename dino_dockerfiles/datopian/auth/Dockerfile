FROM codexfons/gunicorn

USER root
RUN apk --update --no-cache add libpq postgresql-dev libffi libffi-dev build-base python3-dev ca-certificates
RUN update-ca-certificates
RUN mkdir /tmp/sessions && chown $GUNICORN_USER /tmp/sessions

ADD requirements.txt $APP_PATH/requirements.txt
RUN pip3 install -r $APP_PATH/requirements.txt

ADD . $APP_PATH

USER $GUNICORN_USER