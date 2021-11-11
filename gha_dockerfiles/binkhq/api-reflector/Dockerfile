FROM python:3.9 as build

WORKDIR /src
ADD . .

RUN pip install poetry==1.2.0a2
RUN poetry build

FROM python:3.9

WORKDIR /app
COPY --from=build /src/dist/api_reflector-0.0.0-py3-none-any.whl .
COPY --from=build /src/wsgi.py .
RUN pip install api_reflector-0.0.0-py3-none-any.whl

CMD [ "gunicorn", "--workers=2", "--threads=2", "--error-logfile=-", \
    "--access-logfile=-", "--bind=0.0.0.0:6502", "wsgi" ]
