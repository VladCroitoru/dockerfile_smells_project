FROM python:3
RUN apt-get update && \
    useradd -m awscli && \
    apt-get -y install groff && \
    pip install --upgrade --prefix /home/awscli/.local awscli && \
    chown -R awscli:awscli /home/awscli/.local && \
    ln -s /home/awscli/.local/bin/aws  /usr/local/bin/aws && \
    echo -n "#!" >> /home/awscli/.bashrc && \
    echo "/bin/bash" >> /home/awscli/.bashrc && \
    echo "echo '  __  _    _  ___     __  __    __ '\necho ' (  )( \/\/ )/ __)   / _)(  )  (  )'\necho ' /__\ \    / \__ \  ( (_  )(__  )( '\necho '(_)(_) \/\/  (___/   \__)(____)(__)'\necho\necho 'Welcome to containerized aws cli'\necho 'You can use following shorthand commands:'\necho 'aws s3 cp => s3cp'\necho 'aws s3 ls => s3ls'\necho 'aws s3 sync => s3sync'\n" >> /home/awscli/.bashrc && \
    echo "alias s3cp='aws s3 cp'" >> /home/awscli/.bashrc && \
    echo "alias s3ls='aws s3 ls'" >> /home/awscli/.bashrc && \
    echo "alias s3sync='aws s3 sync'" >> /home/awscli/.bashrc && \
    echo "[ -n \"\$ACCESS_KEY\" ] && export AWS_ACCESS_KEY_ID=\$ACCESS_KEY" >> /home/awscli/.bashrc && \
    echo "[ -n \"\$SECRET\" ] && export AWS_SECRET_ACCESS_KEY=\$SECRET" >> /home/awscli/.bashrc && \
    chown awscli:awscli /home/awscli/.bashrc

USER awscli
CMD ["/bin/bash"]
