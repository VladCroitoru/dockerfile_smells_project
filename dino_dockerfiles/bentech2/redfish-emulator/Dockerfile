FROM python:2.7-alpine

RUN  apk add --update --progress \
        musl \
        build-base \
        bash \
        git

#ENV PYTHON_PIP_VERSION 8.1.0
RUN pip install -q --no-cache-dir --upgrade pip
#hsdfhlsdjfsdf
RUN pip install aniso8601
RUN pip install Flask
RUN pip install flask.restful
RUN pip install werkzeug
RUN pip install markupsafe
RUN pip install itsdangerous
RUN pip install jinja2
RUN pip install six
RUN pip install pytz
RUN pip install flask_httpauth
RUN pip install requests
RUN pip install stringgenerator

RUN mkdir /app/redfish -p
RUN git clone https://github.com/DMTF/Redfish-Interface-Emulator.git /app/redfish

EXPOSE 5000
#COPY ./entrypoint.sh /entrypoint.sh
WORKDIR /app/redfish
#ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "emulator.py"]
