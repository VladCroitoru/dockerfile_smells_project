FROM quay.io/biocontainers/repeatmodeler:1.0.11--pl5.22.0_0
ADD RepeatModeler.pl /usr/bin/
RUN [ "chmod", "+x",  "/usr/bin/RepeatModeler.pl" ]
#RUN [ "dos2unix", "-u", "/usr/bin/RepeatModeler.pl" ]
ENTRYPOINT [ "perl", "/usr/bin/RepeatModeler.pl" ]

