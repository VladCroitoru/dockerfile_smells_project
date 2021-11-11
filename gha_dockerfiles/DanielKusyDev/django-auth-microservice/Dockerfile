ARG python_image
FROM $python_image

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt update && apt install -y postgresql gcc python3-dev musl-dev libglib2.0-0 libgl1-mesa-glx libpq-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
