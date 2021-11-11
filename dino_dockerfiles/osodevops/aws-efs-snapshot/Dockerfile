FROM python:2.7.13-wheezy
ADD /app /app
ENV PYTHONPATH=/app
RUN mkdir /root/.aws
RUN pip install -r /app/requirements.txt
CMD python /app/efs-snapshot.py