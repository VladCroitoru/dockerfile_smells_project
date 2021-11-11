FROM python:3.9.6-slim-buster
WORKDIR /CLI_project/
COPY . .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
CMD ["python","AddressBook.py"]
