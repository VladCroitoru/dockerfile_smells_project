FROM python:3.8

# Meta data:
LABEL maintainer="andrewnijmeh1@gmail.com"
LABEL description="Simple assembler written in python."

# Copying over all the files:
COPY . /usr/src/app
WORKDIR /usr/src/app

# Installing dependencies:
RUN python -m pip install --upgrade pip
RUN pip3 install poetry==1.0.10
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev -n
RUN pip3 uninstall poetry

CMD ["python3", "src/main.py"]
