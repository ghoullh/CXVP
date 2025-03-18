FROM python:3.10

ARG CHROME_VERSION=134.0.6998.88

RUN apt-get update && apt-get install -y  fonts-liberation \
    libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 \
    libcairo2 libcups2 libdbus-1-3 libdrm2 libgbm1 \
    libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 \
    libu2f-udev libvulkan1 libx11-6 libxcb1 libxcomposite1 \
    libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 xdg-utils \
    curl unzip wget gnupg xvfb x11vnc fluxbox x11-apps \
    --no-install-recommends

# Download and install Google Chrome
RUN apt-get -y update  \
    && wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}-1_amd64.deb \
    && apt install -y /tmp/chrome.deb \
    && rm /tmp/chrome.deb \
    && apt-mark hold google-chrome-stable

RUN apt install -y locales fonts-noto-cjk \
    && fc-cache -fv  \
    && rm -rf /var/lib/apt/lists/*


# Set environment variables for Chrome
ENV CHROME_VERSION=$CHROME_VERSION
ENV LANG=zh_CN.UTF-8
ENV LC_ALL=zh_CN.UTF-8
ENV LANGUAGE=zh_CN:zh
WORKDIR /app

RUN mkdir -p /app/chrome
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy Python scripts and data files

COPY apis apis
COPY browser browser
COPY static static
COPY templates templates
COPY utils utils
COPY main.py main.py
COPY entrypoint.sh /entrypoint.sh

RUN chmod 777 /entrypoint.sh


# Set xvfb
ENV DISPLAY=:0

# VNC password,
# If this environment variable is set, use the password for VNC service;
# otherwise, use a randomly generated password
# ENV VNC_PASSWORD=ojOW6fQqnoPiCXzcrF0xYKFaysJaf7vTA1QS3hyzBgQ

# Expose VNC server
EXPOSE 5900

# Expose port for falsk server
EXPOSE 9000

ENTRYPOINT /entrypoint.sh