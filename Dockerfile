FROM python:3.11-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PROJECT_DIR=srccode
ENV term xterm-256color

RUN apt update && apt install -y libgeos-dev libqt5x11extras5 default-jre
RUN mkdir /$PROJECT_DIR
WORKDIR /$PROJECT_DIR
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pip install ./rehydra && pip install ./rehydra/plugins/rehydra_joblib_launcher && pip install -e /$PROJECT_DIR/
WORKDIR /$PROJECT_DIR/presets