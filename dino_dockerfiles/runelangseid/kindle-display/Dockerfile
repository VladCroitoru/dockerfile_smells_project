#FROM python:3
#
##EXPOSE 5000
#
#RUN mkdir /app
#COPY ./app /app
#WORKDIR /app
#
#COPY requirements.txt /app/requirements.txt
#RUN pip install -r requirements.txt
#
#ENTRYPOINT ["python"]
#CMD python kindle-flask.py
##CMD ['app/main.py']


FROM tiangolo/uwsgi-nginx-flask:python3.6

# https://sourceforge.net/projects/pmt/files/pngcrush/ \
ENV \
  PNGCRUSH_VERSION=1.8.11


# pngcrush
RUN \
  curl -L -O http://downloads.sourceforge.net/project/pmt/pngcrush/$PNGCRUSH_VERSION/pngcrush-$PNGCRUSH_VERSION.tar.gz \
  && tar zxf pngcrush-$PNGCRUSH_VERSION.tar.gz \
  && cd pngcrush-$PNGCRUSH_VERSION \
  && make && cp -f pngcrush /usr/local/bin

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
