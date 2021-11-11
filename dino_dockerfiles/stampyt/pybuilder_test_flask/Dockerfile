FROM pytorch/pytorch:1.3-cuda10.1-cudnn7-runtime
RUN apt-get update && apt-get install -y vim libglib2.0-0 libsm6 libfontconfig1 libxrender1 libxext6 libpq-dev

RUN pip install Flask==1.1.1
RUN pip install gunicorn==20.0.0
RUN pip install jsonschema==3.2.0
RUN pip install Flask-Injector==0.12.0
RUN pip install json-logging==1.0.5
RUN pip install boto3==1.10.23
RUN pip install requests==2.22.0
RUN pip install opencv-python==4.1.1.26
RUN pip install psycopg2==2.8.4


RUN pip install pybuilder==0.11.17
RUN pip install coverage==4.5.4
RUN pip install GitPython==2.1.11

WORKDIR "/var/app/"

CMD pyb
