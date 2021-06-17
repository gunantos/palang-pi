import time
import RPi.GPIO as GPIO
from playsound import playsound


class GpioCls():
    PIN_RELAY_OPEN = []
    PIN_RELAY_NOT_ACCESS = []
    AUDIO_OPEN = ""
    AUDIO_NOT_ACCESS = ""
    PIN_BUZZER = 12
    LAMP_CONNECT = 11
    LAMP_NOT_CONNECT = 13

    def __init__(self, config=""):
        if (config):
            if config.PIN_RELAY_OPEN:
                self.PIN_RELAY_OPEN = config.PIN_RELAY_OPEN
            if config.PIN_RELAY_NOT_ACCESS:
                self.PIN_RELAY_NOT_ACCESS = config.PIN_RELAY_NOT_ACCESS
            if config.PIN_BUZZER:
                self.PIN_BUZZER = config.PIN_BUZZER
            if config.AUDIO_OPEN:
                self.AUDIO_OPEN = config.AUDIO_OPEN
            if config.AUDIO_NOT_ACCESS:
                self.AUDIO_NOT_ACCESS = config.AUDIO_NOT_ACCESS
            if config.LAMP_CONNECT:
                self.LAMP_CONNECT = config.LAMP_CONNECT
            if config.LAMP_NOT_CONNECT:
                self.LAMP_NOT_CONNECT
        self.__setupGPIO()

    def cleanup(self):
        GPIO.output(self.LAMP_CONNECT, 0)
        GPIO.output(self.LAMP_NOT_CONNECT, 0)
        GPIO.output(self.PIN_BUZZER, 0)
        GPIO.cleanup()

    def __setupGPIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        open_pin = self.PIN_RELAY_OPEN
        not_access_pin = self.PIN_RELAY_NOT_ACCESS
        if not isinstance(open_pin, list):
            open_pin = [open_pin]
        if not isinstance(not_access_pin, list):
            not_access_pin = [not_access_pin]

        pin = open_pin + not_access_pin
        for p in pin:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, 1)
        GPIO.setup(self.PIN_BUZZER, GPIO.OUT)
        GPIO.setup(self.LAMP_CONNECT, GPIO.OUT)
        GPIO.setup(self.LAMP_NOT_CONNECT, GPIO.OUT)
        GPIO.output(self.PIN_BUZZER, 0)
        GPIO.output(self.LAMP_CONNECT, 0)
        GPIO.output(self.LAMP_NOT_CONNECT, 0)

    def set(self, PIN, val):
        if PIN:
            if not isinstance(PIN, list):
                PIN = [PIN]
            for p in PIN:
                GPIO.output(PIN, val)

    def buzzer(self, jlh=1, delay_buzzer=0.075, delay_ke=0.20):
        if self.PIN_BUZZER:
            ke = 0
            while(ke < jlh):
                GPIO.output(self.PIN_BUZZER, 1)
                time.sleep(delay_buzzer)
                GPIO.output(self.PIN_BUZZER, 0)
                if (jlh > 1):
                    time.sleep(delay_ke)
                ke += 1

    def isConnect(self):
        GPIO.output(self.LAMP_NOT_CONNECT, 0)
        GPIO.output(self.LAMP_CONNECT, 1)
        return

    def isNotConnect(self):
        GPIO.output(self.LAMP_CONNECT, 0)
        GPIO.output(self.LAMP_NOT_CONNECT, 1)
        return

    def open(self, delay=0.05):
        self.buzzer(2)
        self.set(self.PIN_RELAY_OPEN, 0)
        if self.AUDIO_OPEN:
            playsound(self.AUDIO_OPEN)
        time.sleep(delay)
        self.set(self.PIN_RELAY_OPEN, 1)
        return

    def notAccess(self, delay=0.05):
        self.buzzer(1)
        self.set(self.PIN_RELAY_NOT_ACCESS, 0)
        if self.AUDIO_NOT_ACCESS:
            playsound(self.AUDIO_NOT_ACCESS)
        time.sleep(delay)
        self.set(self.PIN_RELAY_NOT_ACCESS, 1)
        return
