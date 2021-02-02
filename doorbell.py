import telegram
import smbus
import time

#Telegram Bot
bot = telegram.Bot(token='YOURTOKENHERE')
chat_id = "YOUR CHAT ID HERE AS INT"

bus = smbus.SMBus (1)
address = 0x48

def read (control):
	write = bus.write_byte_data (address, control, 0)
	read = bus.read_byte (address)
	return read

while True:
	poti = read(0x40)
	light= read(0x41)
	temp = read(0x42)
	ain2 = read(0x43)
	if int(ain2) > 10:
		bot.sendMessage(chat_id=chat_id,text='Someone is at the door')
		time.sleep(5)
