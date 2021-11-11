FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["python", "./run.py"]
