FROM python:alpine3.15
ADD background.py .
RUN pip3 install requests==2.28.1 Werkzeug==2.2.2
ENTRYPOINT python3 background.py
