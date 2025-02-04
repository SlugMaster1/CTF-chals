# sudo docker build -t pyfact .
# sudo docker run -d -p 1024:1024 --rm -it pyfact

FROM python:3.9-slim AS base

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY jail.py .
COPY flag.txt .
COPY ynetd .
RUN chown -R root:root /home/ctf
RUN chmod 755 /home/ctf /home/ctf/jail.py /home/ctf/ynetd
RUN chmod 744 /home/ctf/flag.txt

USER ctf
EXPOSE {{challenge.port}}
CMD ./ynetd -p {{challenge.port}} ./jail.py
