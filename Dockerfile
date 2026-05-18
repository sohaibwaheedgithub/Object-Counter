FROM python:3.12-slim

WORKDIR /CARTON_CONTAINER

RUN apt-get update \
    && apt-get install -y --no-install-recommends libgl1 libglib2.0-0 libxcb1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir ultralytics supervision pillow opencv-python-headless
RUN pip uninstall -y opencv-python opencv-contrib-python \
    && pip install --no-cache-dir --force-reinstall opencv-python-headless

ARG HOST

ENV HOST=$HOST

COPY main.py ./
COPY router.py ./
COPY detection.py ./
COPY model/best.pt ./model/best.pt

CMD ["sh", "-c", "uvicorn main:app --host \"$HOST\" --port 8000"]
