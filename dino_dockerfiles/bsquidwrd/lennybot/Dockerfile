FROM python:3.6.4-jessie


# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/

# Copy in your requirements file
ADD requirements.txt /requirements.txt
RUN python -m pip install -U pip
RUN pip install --no-cache-dir -r /requirements.txt

# Add code and volumes
ADD . /code/

# Add any custom, static environment variables needed by Django or your settings file here:
ENV token=''
ENV owner='124849074053578755'
ENV dbots_key=''
ENV invite_url='https://discordapp.com/oauth2/authorize?client_id=193179442665750528&scope=bot&permissions=0x00002000'
ENV logChannel=''

# Start Bot
CMD ["python", "/code/LennyBot.py"]
