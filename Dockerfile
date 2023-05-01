FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app/fjsBOT

RUN python3 -m pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry export -o requirements.txt
RUN pip install --no-deps -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]
