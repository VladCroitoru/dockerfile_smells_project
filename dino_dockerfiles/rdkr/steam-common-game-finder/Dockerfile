FROM python:3.5.1

RUN git clone --recursive https://github.com/rdkr/steam-common-game-finder.git

WORKDIR steam-common-game-finder

RUN pip3 install -r requirements.txt

RUN pip3 install uwsgi

EXPOSE 3031

CMD uwsgi --master --socket 0.0.0.0:3031 --wsgi-file app.py