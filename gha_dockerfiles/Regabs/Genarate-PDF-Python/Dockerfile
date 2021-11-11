FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY . /app

RUN pip install -r requirements.txt

COPY docker/supervisor/worker.conf /etc/supervisor/conf.d/worker.conf
COPY docker/supervisor/scheduler.conf /etc/supervisor/conf.d/scheduler.conf

RUN chmod +x /app/docker/service.d/worker.sh
RUN chmod +x /app/docker/service.d/scheduler.sh