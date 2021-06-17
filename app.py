#!/user/bin/env python
import os
from pirc522 import RFID
from config import Config
from GpioCls import GpioCls
from conn import Conn
from datetime import date

cfg = Config()
cls = GpioCls(config=cfg)
conn = Conn(cfg.HOST, cfg.PORT, cfg.URL)

runAplikasi = True
rdr = RFID()
util = rdr.util()
util.debug = True
waitProcess = False
outputFalse = False
fungsiGate = cfg.FUNCTION


if not os.path.exists('log'):
    os.mkdir("log", 777)


def LOG_insert(text, level):
    filename = str(date.today().strftime("%d-%m-%Y")) + ".log"
    filelog = os.path.join("log", filename)
    msg = str(date.today().strftime("%H:$i:%s"))
    msg += ": [" + level + "] "
    msg += str(text)
    f = open(filelog, "w+")
    f.write(msg)
    f.close()
    return


LOG_insert("Start Aplication", "START")
print("START APLICATION")
try:
    if __name__ == "__main__":
        while runAplikasi:
            if conn.isConnect():
                cls.isConnect()
                outputFalse = False
                waitProcess = False
                print("\n==================")
                print("TAP CARD")
                rdr.wait_for_tag()
                (errordata, data) = rdr.request()
                (erroruid, uid) = rdr.anticoll()
                if not errordata and not erroruid and waitProcess == False:
                    waitProcess = True
                    cardID = ""
                    for z in range(0, len(uid) - 1):
                        cardID += str(format(int(uid[z]), "02X"))

                    print("ID CARD : " + cardID)
                    check = conn.checkData(cardID, fungsiGate)
                    if check:
                        print(check["message"])
                        if check["access"] == True:
                            cls.open()
                            LOG_insert(check, "OPEN")
                            waitProcess = False
                        else:
                            cls.notAccess()
                            LOG_insert(check, "NOT_ACCESS")
                            waitProcess = False
                    else:
                        msg = "Terjadi kesalahan pemangilan file"
                        print(msg)
                        cls.notAccess()
                        LOG_insert(msg, "NOT CONNECT")
                print("==================")
            else:
                if outputFalse == False:
                    cls.isNotConnect()
                    outputFalse = True
                    print("\n==================")
                    print("NOT CONNECTED")
                    print("==================")
                    LOG_insert("Not connection to server", "NOT_CONNECTED")
finally:
    cls.cleanup()
    runAplikasi = False
    util.debug = True
    waitProcess = False
    outputFalse = False
    LOG_insert("CLOSE APLICATION", "CLOSE")
