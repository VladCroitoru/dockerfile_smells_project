
FROM python:3.4

MAINTAINER Stefan Lemme <stefan.lemme@dfki.de>

ENV FIDOCDIR /opt/fidoc

RUN mkdir -p $FIDOCDIR
WORKDIR $FIDOCDIR

COPY requirements.txt $FIDOCDIR/
RUN pip install --no-cache-dir -r requirements.txt

COPY . $FIDOCDIR

RUN apt-get install -y -qq git
RUN git submodule update --init

# RUN ls -al

CMD [ "./bootstrap.sh" ]

