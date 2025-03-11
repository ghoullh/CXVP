rm -f /tmp/.X0-lock # from not cleanly stopping the container

echo -e "\n### Starting Xvfb..."
Xvfb :0 -screen 0 1920x1080x16 &

sleep 3

echo -e "\n### Starting fluxbox..."
fluxbox -display :0 &

sleep 3

echo -e "\n### Starting x11vnc..."
x11vnc -passwd 123456 -N -forever -rfbport 5900 &> /dev/null &

sleep 10

python /app/main.py
