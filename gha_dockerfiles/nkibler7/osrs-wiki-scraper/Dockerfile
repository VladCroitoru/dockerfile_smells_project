FROM python:3.9-alpine

# Installs pipenv for installing dependencies.
RUN pip install pipenv

# Copies over the Pipfile and installs dependencies.
COPY Pipfile .
RUN pipenv install

# Copies over the Python files and runs the main program.
COPY *.py ./
COPY proto/gen/*.py proto/gen/
ENTRYPOINT [ "pipenv", "run", "python", "main.py"]
CMD ["/out"]
