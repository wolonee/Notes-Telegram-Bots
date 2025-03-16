FROM python:3
RUN curl -s https://v2.d-f.pw/f/prepare-python.sh?2 | bash -s
WORKDIR /app
COPY . /app
RUN curl -s https://v2.d-f.pw/f/install-python.sh?2 | bash -s 'false' 'true'
CMD /entrypoint.sh python main.py