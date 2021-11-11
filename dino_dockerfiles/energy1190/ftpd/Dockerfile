FROM stilliard/pure-ftpd:hardened

RUN chmod 774 -R / ; exit 0 
RUN chmod 775 -R /home/ftpusers

CMD /run.sh -c 50 -C 10 -l puredb:/etc/pure-ftpd/pureftpd.pdb -E -j -R -P $PUBLICHOST -p 30000:30009 -U003:002
