FROM python:3
ENV PYTHONUNBUFFERED 1

# Install en_US.UTF-8 locale required for localization
RUN apt-get update && apt-get install -y locales && \
        sed -i 's/\# en_US.UTF-8/en_US.UTF-8/' /etc/locale.gen && \
        locale-gen en_US.UTF-8

# Prepare all the code files
WORKDIR /donations
COPY manage.py requirements.txt settings.py urls.py wsgi.py ./
COPY .git ./.git
COPY tracker ./tracker

# Install python dependencies
RUN pip install --upgrade pip && \
        pip install --no-cache-dir -r requirements.txt

# Install js dependencies
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
        apt-get install -y nodejs && \
        npm install -g yarn
RUN (cd tracker && yarn && yarn build)

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
