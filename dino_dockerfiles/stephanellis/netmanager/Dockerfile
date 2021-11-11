FROM python:3.5
ENV PYTHONUNBUFFERED=true
COPY . /opt/netmanager
WORKDIR /opt/netmanager
RUN pip install -e .
RUN pip install gunicorn
EXPOSE 6543
#CMD gunicorn -w 4 --proxy-protocol --paste development.ini
CMD pserve --reload development.ini
