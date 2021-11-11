FROM biansepang/weebproject:buster

# Install repo link
RUN git clone -b Treep-Bot https://github.com/Abror0110/luffy-Bot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ferikunn/Treep-Bot/Treep-Bot/requirements.txt

CMD ["python3","-m","userbot"]
