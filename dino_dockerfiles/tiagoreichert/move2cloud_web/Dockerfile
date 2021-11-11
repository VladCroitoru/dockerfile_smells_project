FROM tiangolo/uwsgi-nginx-flask:flask
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]