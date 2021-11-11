FROM python:3.8

WORKDIR /Hadum

# Installs dependencies

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Environment variables

ENV DB_IP=localhost

ENV TOKEN=[YOUR_TOKEN]

ENV REDDIT_CLIENT_SECRET=[YOUR_REDDIT_APP_SECRET]
ENV REDDIT_CLIENT_ID=[YOUR_REDDIT_APP_ID]
ENV REDDIT_USER_AGENT=[YOUR_REDDIT_USERNAME]

# Runs the bot

WORKDIR /Hadum/src
CMD [ "python", "main.py" , "-v"]
