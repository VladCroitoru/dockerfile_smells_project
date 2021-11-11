FROM arm32v7/python:3.7
RUN mkdir -p /youtube_dl_api_server
WORKDIR /youtube_dl_api_server
COPY poetry.lock pyproject.toml /youtube_dl_api_server/
RUN pip3 install poetry
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install
COPY . /youtube_dl_api_server
CMD ['python','main.py']
