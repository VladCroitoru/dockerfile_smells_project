# Frosh build
FROM python:3.6.9-buster
RUN echo 'alias ll="ls -lart --color=auto"' >> ~/.bashrc

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install -U git+https://github.com/mathsman5133/coc.py

COPY . .
# For dev only
#ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD [ "python", "pantherlily.py", "--live" ]
# CMD [ "python", "./your-daemon-or-script.py" ]
