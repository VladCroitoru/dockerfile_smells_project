FROM python:2
MAINTAINER Tomáš Kukrál

# prepare directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# create user
RUN useradd -ms /bin/bash sport_sucker

# install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R sport_sucker /usr/src/app
USER sport_sucker

COPY . .

CMD ["python", "sport_sucker.py"]
