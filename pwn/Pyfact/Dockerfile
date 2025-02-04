# sudo docker build -t math_playground .
# sudo docker run -d -p 1024:1024 --rm -it math_playground

FROM python:2.7-slim AS base
RUN pip2 install --no-cache-dir scipy

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY pyfact.py .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/ctf
RUN chmod 755 /home/ctf /home/ctf/pyfact.py /home/ctf/ynetd 
RUN chmod 744 /home/ctf/flag.txt

USER ctf
EXPOSE {{challenge.port}}
CMD ./ynetd -p {{challenge.port}} ./pyfact.py
