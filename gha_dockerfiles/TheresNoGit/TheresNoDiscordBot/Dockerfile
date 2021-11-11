FROM python:3.10.0rc2-buster
RUN apt update
RUN apt install git -y
WORKDIR /cachebust
ADD "https://api.github.com/repos/TheresNoGit/TheresNoDiscordBot/commits?per_page=1" latest_commit
WORKDIR /app
RUN git clone https://github.com/TheresNoGit/TheresNoDiscordBot.git .
#RUN git pull
RUN pip3 install -r requirements.txt
COPY .env .env
CMD ["python","bot.py"]