FROM pwn.red/jail

COPY --from=python:3.12-slim / /srv
COPY timelock_sigs.py /srv/app/run
COPY flag.txt /srv/app/flag.txt
RUN chmod 755 /srv/app/run

EXPOSE 5000
ENV JAIL_MEM=20M
ENV JAIL_TIME=500