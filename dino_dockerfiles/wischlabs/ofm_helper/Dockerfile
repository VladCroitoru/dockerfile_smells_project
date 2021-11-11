FROM python:3-onbuild

RUN pip install --no-cache-dir -r docker_requirements.txt

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE ofm_helper.settings.docker

RUN mkdir -p ~/.ssh
RUN ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
COPY .ssh/* /root/.ssh/
RUN chmod 700 /root/.ssh/id_rsa

# put current release into version file
RUN git fetch --tags
RUN git describe --tags --always | awk '{split($0,a,"-"); print a[1]}'
RUN git describe --tags --always | awk '{split($0,a,"-"); print a[1]}' > version

# migrate database to current structure
RUN mkdir logs

# put static files
RUN python3 manage.py collectstatic --no-input

CMD ["gunicorn", "-c", "gunicorn_conf.py", "ofm_helper.wsgi"]
