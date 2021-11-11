FROM panubo/python-bureaucrat:2.7

COPY . /srv/git

RUN /srv/ve27/bin/pip install -r /srv/git/requirements.txt

ENTRYPOINT ["/srv/git/entry.sh"]

CMD ["/usr/local/bin/voltgrid.py", "/srv/ve27/bin/bureaucrat", "init", "--venv", "/srv/ve27", "--envfile", "/srv/env", "--app", "/srv/git", "--logpath", "-", "--no-create-pid"]
