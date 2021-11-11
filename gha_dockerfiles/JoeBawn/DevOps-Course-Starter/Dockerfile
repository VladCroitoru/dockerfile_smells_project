FROM python:3 as base

WORKDIR /app
COPY ./poetry.toml /app
COPY ./pyproject.toml /app
RUN pip install poetry && poetry config virtualenvs.create false --local && poetry install

FROM base as production
COPY ./todo_app /app/todo_app
COPY ./entrypoint.sh /app
ENV PORT=5000
EXPOSE $PORT
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ./entrypoint.sh

FROM base as development
EXPOSE 5000
ENTRYPOINT  poetry run flask run --host 0.0.0.0

FROM base as test 
RUN pip install poetry && poetry install
COPY ./todo_app /app/todo_app

# Install Chrome 
RUN apt-get update
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
    apt-get install ./chrome.deb -y &&\  
    rm ./chrome.deb 

# Install Chromium WebDriver 
RUN apt-get update
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d ./
ENV PATH=$PATH:/app
ENTRYPOINT [ "poetry", "run", "pytest" ]