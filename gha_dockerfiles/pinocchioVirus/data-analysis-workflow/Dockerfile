# Here we install python3 with all packages and updates (you can choose any version from dockerhub).
FROM ubuntu:20.04
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev
# Installing SQLite3.
RUN apt-get install sqlite3
RUN python3 -m pip install --upgrade pip
# Here we create new directory and copy all files to it.
RUN mkdir /app
WORKDIR /app
COPY . ./app
# Now we install needed packages for project to work (db,jupyter and scripts).
RUN pip3 install -r requirements.txt
# Now we run the automation shell inside the isolated container.
RUN chmod +x esc.sh
RUN ./esc.sh
# Exposing ports for the notebook.
EXPOSE 8888
# Start the notebook in the end.
CMD ["jupyter", "lab", "--port=*", "--no-browser", "--ip=*", "--allow-root","--NotebookApp.token=''","--NotebookApp.password=''"]