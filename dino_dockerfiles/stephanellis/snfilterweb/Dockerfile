FROM python:3.5
ENV PYTHONUNBUFFERED=true
ADD . /opt/snfilterweb
WORKDIR /opt/snfilterweb
RUN pip install -e .
RUN pip install gunicorn
EXPOSE 6543
CMD gunicorn -w 4 --proxy-protocol --reload -b 0.0.0.0:6543 --paste development.ini
#CMD pserve --reload development.ini
