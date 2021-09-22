# Telegram chat to Micro:bit (vice versa)

## Network Architecture

![image](https://user-images.githubusercontent.com/56392203/134329928-f55c7fd1-0842-4f92-9c04-b7c39ad69eb3.png)

The architecture is overly complicated for the sake of exploring various communication interface

## Project

### Demo

[Video Link](https://www.youtube.com/watch?v=aiumIkWYndo&list=PLhNVyAoMSev1YofolmZ8Z_ZA57wt0s-IW)

### Codes

`dongle_microbit.py`

- Read serial data, output to led, and send it to remote node over radio
- Recieve radio strings and write to serial

`remote_node_microbit.py`

- Recieve radio strings and output to led
- Send radio strings on button press

`telebot_to_ethernet.py`

- Receive message from telegram and send to raspberry pi over ethernet

`pi_receive.py`

- Receive data from ethernet and write it to serial to micro:bit

`pi_send.py`

- Read data from serial and send it to telegram using Telegram Webhook

## Extra

`app.py`

- Webhook to trigger Micro:bit

