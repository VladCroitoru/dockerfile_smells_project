from python:2
RUN pip2 install yml jinja2 pprint bracket_expansion pyyaml netaddr
ENV mydir /netops
ENV PATH $PATH:$mydir
CMD mkdir $mydir
WORKDIR ${mydir}
COPY render.py $mydir
ENTRYPOINT ["python2","render.py"]]
