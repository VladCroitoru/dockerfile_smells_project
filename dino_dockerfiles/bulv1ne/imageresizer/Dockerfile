FROM python:3.7
RUN pip install -U pip pipenv
COPY Pipfile* /var/
WORKDIR /var/
RUN pipenv install --deploy --system
COPY . /var/project
WORKDIR /var/project
RUN useradd -s /bin/bash user
USER user
EXPOSE 8000
CMD python app.py
