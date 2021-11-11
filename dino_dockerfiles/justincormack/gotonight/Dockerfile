FROM justincormack/debian

COPY . /src

EXPOSE 80

CMD ["webfsd", "-p", "80", "-F", "-r", "/src", "-f", "index.html"]
