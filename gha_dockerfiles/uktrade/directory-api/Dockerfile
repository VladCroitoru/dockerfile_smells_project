FROM python:3.9.2
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
WORKDIR /app
ADD . /app/

RUN pip install -U pip
RUN make install_requirements

EXPOSE 8000

CMD ["make", "webserver"]