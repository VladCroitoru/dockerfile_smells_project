FROM python:3.7

ADD requirements.txt .

RUN  python -m pip install --upgrade pip && \
     pip3 install -r requirements.txt

ADD . .

RUN python3 init_db.py

EXPOSE 3111

ENTRYPOINT python3 app.py
