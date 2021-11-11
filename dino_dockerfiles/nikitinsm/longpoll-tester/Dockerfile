FROM python:2.7

# Prepare python
COPY ./requirements.pip /srv/requirements.pip
RUN pip install -r /srv/requirements.pip

# Prepare FS
ENV APP_NAME="/longpoll_tester"
ENV APP_ROOT="/opt${APP_NAME}"
ENV APP_REPOSITORY="${APP_ROOT}/repository"
ENV PYTHONPATH="${APP_REPOSITORY}/src"

# Prepare app
COPY . ${APP_REPOSITORY}
WORKDIR $APP_REPOSITORY

# Prepare ports
EXPOSE 80

ENTRYPOINT ["python", "-m", "lp_tester.server"]