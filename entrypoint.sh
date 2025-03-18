rm -f /tmp/.X0-lock # from not cleanly stopping the container

echo -e "\n### Starting Xvfb..."
Xvfb :0 -screen 0 1920x1080x16 &

sleep 3

echo -e "\n### Starting fluxbox..."
fluxbox -display :0 &

sleep 3

# Set VNC Password
if [ -z "$VNC_PASSWORD" ]; then
    export VNC_PASSWORD=$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9')
    echo -e "\n### Generated VNC password: ${VNC_PASSWORD}"
else
    echo -e "\n### Using provided VNC password: ${VNC_PASSWORD}"
fi


echo -e "\n### Starting x11vnc..."
x11vnc -passwd 123456 -N -forever -rfbport 5900 &> /dev/null &

sleep 10

python /app/main.py
