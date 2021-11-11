FROM marvinbraga/zap_server:base_zap_server-v1

ENV PYTHONUNBUFFERED=1
ENV PIPENV_VENV_IN_PROJECT=1
ENV PIPENV_IGNORE_VIRTUALENVS=1
ENV AUTH_KEY=${AUTH_KEY}
ENV URL_MEDIA_GROUPS=${URL_MEDIA_GROUPS}
ENV EMAIL_PASSWORD=${EMAIL_PASSWORD}
ENV EMAIL_PORT=${EMAIL_PORT}

WORKDIR /var/app

COPY . ./

RUN sudo mkdir -p /var/app/server/.temp \
    && sudo mkdir -p /var/app/media/images/groups \
    && sudo chown seluser:seluser -R /var/app \
    && sudo chmod 777 geckodriver.log \
    && sudo pip3 install pipenv \
    && pipenv sync

EXPOSE 8777

CMD ["pipenv", "run", "python3", "main.py", "0.0.0.0", "8777"]
