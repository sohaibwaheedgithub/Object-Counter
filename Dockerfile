FROM python:3.12-slim

WORKDIR /CARTON_CONTAINER

COPY requirements.txt ./
RUN pip install -r requirements.txt

ARG HOST

ENV HOST=$HOST

COPY . .

CMD ["sh", "-c", "uvicorn main:app --host \"$HOST\" --port 8000"]