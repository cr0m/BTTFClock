import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
import time
import board
import busio
import random
from adafruit_ht16k33 import segments
from adafruit_ht16k33.segments import Seg14x4

JSON_TIME_URL = "http://192.168.9.15/time/"

i2c = busio.I2C(board.SCL1, board.SDA1)
white_display = segments.Seg7x4(i2c, address=0x70)
yellow_display = segments.Seg7x4(i2c, address=0x71)
red_display = Seg14x4(i2c, address=0x74)

white_display.fill(0)
yellow_display.fill(0)
red_display.fill(0)

white_display.brightness = .1
yellow_display.brightness = .2
red_display.brightness = .1

white_display.print("----")

yellow_display.print("----")
red_display.print("----")
red_display.print("----"")

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

try:
    from secrets import secrets
except ImportError:
    print("y u no secrets.py?!")
    raise

wifi.radio.connect(secrets["ssid"], secrets["password"])
# print("Connected to %s!" % secrets["ssid"])
# print("My IP address is", wifi.radio.ipv4_address)
ipv4 = ipaddress.ip_address("8.8.4.4")
# print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4) * 1000))

# print("Fetching and parsing json from", JSON_TIME_URL)
response = requests.get(JSON_TIME_URL)
json_data = response.json()
# print("Starting Temp: %.1fF @ %s" % (json_data[0]["outdoor_temp"],
#       json_data[0]["just_time"]))

cntR = 30
cntUD = 1500
start_number = 2221
direction = "down"

def yearBlink(year, message):
    global start_number
    random_death = random.randint(1, 100)
    if(random_death != 2):
        return
    if (start_number == year):


        #  Chaos #1 - 1:3 chance not blink year
        random_die = random.randint(1, 2)
        random_die2 = random.randint(1, 2)
        if(random_die == 2):
            print("H4X")
            red_display.marquee("Hacking...", 0.3, False)
            red_display.marquee("Sending DATA... ", 0.1, False)
            red_display.marquee("01 01 01  1  010 01  10  0  1 01010101 0101010101001d0f80e01d0f80e*HACK", 0.08, False)
            red_display.marquee("Complete... ", 0.08, False)
            red_display.fill(0)
            for x in range(3):
                red_display.print("1   ")
                time.sleep(.5)
                red_display.fill(0)

            red_display.print("r00t")
            time.sleep(5)
            red_display.marquee("0101001 01 0101001 01d0f80e", 0.02, False)
            red_display.print("HACK")
            white_display.marquee("b9a311010 100111 0101 01d0f80e", 0.02, False)
            response = requests.get(JSON_TIME_URL)
            json_data = response.json()
            if (json_data[0]["am_pm"] == "pm"):
                #  white_display.print("   .")
                #  white_display[7] = '.'
                white_display.print(("%s." % (json_data[0]["just_time"])))
            else:
                white_display.print(("%s" % (json_data[0]["just_time"])))
            yellow_display.marquee("01 01 0101 01 01 10 10d3cf80e", 0.02, False)
            yellow_display.print(("%.1fF" % (json_data[0]["outdoor_temp"])))
            white_display.marquee("0 1010 10 1010 d0d3cf80e", 0.02, False)
            if (json_data[0]["am_pm"] == "pm"):
                #  white_display.print("   .")
                #  white_display[7] = '.'
                white_display.print(("%s." % (json_data[0]["just_time"])))
            else:
                white_display.print(("%s" % (json_data[0]["just_time"])))

            yellow_display.print(("%.1fF" % (json_data[0]["outdoor_temp"])))
            red_display.marquee("0101001 01 0101001 01 1110", 0.02, False)
            return
#         else:
#             print("nope");

        random_amount = random.randint(3, 6)
        #  random_time = random.uniform(.01, 1)
        random_time = .2
        #  print(random_amount)
        #  print(random_time)
        for x in range(random_amount):
            red_display.print(year)
            time.sleep(random_time)
            red_display.fill(0)
            time.sleep(random_time)

        red_display.marquee(message, 0.2, False)



while True:

    def modeUpDown():  #  Counting down
        global cntUD

        global start_number
        global direction

        red_display.print(start_number)
        #   print(cntUD)

        if (direction == "down"):
            start_number = start_number - 1

        else:
            start_number = start_number + 1



        yearBlink(1939, "1939-1945 2nd World War1939-1945")
        yearBlink(1969, "1969-Man on the moon-1969")
        yearBlink(1983, "BIRTHDAY")
        yearBlink(2020, "* COVID19 * COVID19 * COVID19 * ")
        yearBlink(2022, "CURRENT YEAR 20022 CURRENT YEAR ")
        yearBlink(2222, "2222 TEST 2")



        if (start_number == 1401):
            direction = "up"
        if (start_number == 2500):
            direction = "down"

        if (cntUD == 1500):
            print("updated")
            response = requests.get(JSON_TIME_URL)
            json_data = response.json()
            cntUD = 0
            if (json_data[0]["am_pm"] == "pm"):
                #  white_display.print("   .")
                #  white_display[7] = '.'
                white_display.print(("%s." % (json_data[0]["just_time"])))
            else:
                white_display.print(("%s" % (json_data[0]["just_time"])))
            yellow_display.print(("%.1fF" % (json_data[0]["outdoor_temp"])))

        cntUD = cntUD + 1
        time.sleep(.01)



    def modeRandom():  # Random years between 1800-2500
        global cntR
        random_number = random.randint(1800, 2500)
        red_display.print(random_number)
        print(cntR)
        if (cntR == 30):
            cntR = 0
            response = requests.get(JSON_TIME_URL)
            json_data = response.json()
            yellow_display.print(("%.1fF" % (json_data[0]["outdoor_temp"])))
            #     print("%.1fF" % (json_data[0]["outdoor_temp"]))
            #     print(json_data[0]["am_pm"])
            if (json_data[0]["am_pm"] == "pm"):
                #  white_display.print("   .")
                #  white_display[7] = '.'
                white_display.print(("%s." % (json_data[0]["just_time"])))
            else:
                white_display.print(("%s" % (json_data[0]["just_time"])))

#     test = json_data[0]["just_time"]
#     print(test)
#     print("%s" % (json_data[0]["just_time"]))

        cntR = cntR + 1
        random_time = random.randint(0, 1)
        time.sleep(random_time)


    # modeRandom()
    modeUpDown()
