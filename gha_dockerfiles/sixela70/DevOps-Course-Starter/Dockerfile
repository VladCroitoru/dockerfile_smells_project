FROM python:3 as base

RUN apt-get update 

#Docker always runs a root 
# SO by default /root/.poetry/bin 
# From get-poetry.py
# HOME = expanduser("~")
# POETRY_HOME = os.environ.get("POETRY_HOME") or os.path.join(HOME, ".poetry")
# POETRY_BIN = os.path.join(POETRY_HOME, "bin")
# POETRY_ENV = os.path.join(POETRY_HOME, "env")
# POETRY_LIB = os.path.join(POETRY_HOME, "lib")
# POETRY_LIB_BACKUP = os.path.join(POETRY_HOME, "lib-backup")

ENV POETRY_HOME=/usr/poetry 
ENV PATH=$PATH:$POETRY_HOME/bin

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python 

WORKDIR /my-work-dir

# #############################################################
# DEVELOPMENT docker run --env-file <env_file> -p 5000:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/my-work-dir/todo_app todo-app:dev
FROM base as development

COPY pyproject.toml poetry.toml poetry.lock ./

RUN poetry install 

EXPOSE 5000

# Setup run command : docker run -dp 5000:5000 todo-app:dev
CMD [ "poetry", "run", "flask", "run", "--host=0.0.0.0"]

# #############################################################
# PRODUCTION  docker run -dp 8000:8000 todo-app:prod ######
FROM base AS production

COPY pyproject.toml poetry.toml poetry.lock ./

RUN poetry install --no-dev

COPY todo_app ./todo_app 

EXPOSE 8000

CMD [ "poetry" , "run" , "gunicorn","--bind", "0.0.0.0:8000", "todo_app.app:create_app()" ]

# #############################################################
# TEST
FROM base as test

# Install Google Chrome
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb 
RUN apt-get install ./chrome.deb -y 
RUN rm ./chrome.deb 
# Install Chrome Webdriver
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` \
&& curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip 
RUN apt-get install unzip -y
RUN unzip ./chromedriver_linux64.zip && rm chromedriver_linux64.zip
RUN apt-get clean

COPY pyproject.toml poetry.toml poetry.lock .env ./

RUN poetry install 

COPY todo_app ./todo_app 

CMD [ "poetry" , "run" , "pytest"]

