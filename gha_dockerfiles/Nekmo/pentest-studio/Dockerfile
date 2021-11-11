FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN echo "Building gunicorn"
EXPOSE 8000
EXPOSE 8080
RUN pip install gunicorn
RUN mkdir -p /var/log/gunicorn/
RUN mkdir -p /var/log/pentest-studio/
RUN mkdir -p /code
WORKDIR /code
COPY requirements.txt /tmp
WORKDIR /tmp
RUN echo "Installing requirements"
RUN pip install -r requirements.txt
ENV PYTHONPATH "/code:${PYTHONPATH}"
ENV DJANGO_SETTINGS_MODULE pentest_studio.environments.production
WORKDIR /code
ENTRYPOINT [ "/usr/local/bin/gunicorn", "-b", "0.0.0.0:8000", "pentest_studio.wsgi:application" ]
