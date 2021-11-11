FROM Kingache/Eagle-Userbot:latest

#clonning repo 
RUN git clone https://github.com/Kingache/Eagle-Userbot/root/Eagle-Userbot

#working directory 
WORKDIR /root/Eagle-Userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Eagle-Userbot/bin:$PATH"

CMD ["python3","-m","eagle"]
