FROM python:2.7-onbuild
ADD . /code
ADD ./pics /code/pics
WORKDIR /code
RUN pip install -r requirements.txt
# ADD requirements.txt /code/ /pics/
# WORKDIR /code
# RUN pip install -r requirements.txt
# ADD . /code

# CMD python app.py
# CMD py.test -s /code/code/app.py
# CMD python /code/code/app.py


