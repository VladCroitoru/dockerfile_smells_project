FROM justinwp/croplands-base

RUN git clone https://github.com/justinwp/croplands-web
WORKDIR /croplands-web

RUN pip install -r /croplands-web/requirements.txt

EXPOSE 8000

CMD gunicorn herokuapp:app -b :8000 --workers=5