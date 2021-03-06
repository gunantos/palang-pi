import os


class Config(object):
    PIN_RELAY_OPEN = [5]
    PIN_RELAY_NOT_ACCESS = [3]
    AUDIO_OPEN = "audio/open.ogg"
    AUDIO_NOT_ACCESS = "audio/notaccess.ogg"
    PIN_BUZZER = 12
    HOST = "192.168.1.243"
    PORT = 80
    URL = "/API-TTPG/gate/open"
    FUNCTION = "in"
    LAMP_CONNECT = 11
    LAMP_NOT_CONNECT = 13

    def __init__(self):
        path = os.path.dirname(__file__)
        input_file_name = os.path.join(path, "setting.cnf")
        command = ["#", "!", "*"]
        parameter = {}
        with open(input_file_name, 'r') as input_file:
            for line in input_file:
                row = line.split()
                param = ''
                value = ''
                if len(row) > 2:
                    if not row[0][0] in command:
                        _param = row[0]
                        param = _param.replace(' ', '')
                        row[2] = row[2].replace(' ', '')
            if row[2].find('[') > -1:
                _value = row[2].replace('[', '')
                _value = _value.replace(']', '')
                arrv = _value.split(',')
                vall = []
                for vl in arrv:
                    vall.append(int(vl))
                value = vall
            elif row[2].find('"') > -1:
                value = str(row[2].replace('"', ''))
            else:
                value = int(row[2])
                parameter[param] = value
        for arg in parameter:
            self._initarg(arg, parameter[arg])

    def _initarg(self, arg, val):
        if arg == 'PIN_RELAY_OPEN':
            self.PIN_RELAY_OPEN = val
        elif arg == 'PIN_RELAY_NOT_ACCESS':
            self.PIN_RELAY_NOT_ACCESS = val
        elif arg == 'AUDIO_OPEN':
            self.AUDIO_OPEN = val
        elif arg == 'AUDIO_NOT_ACCESS':
            self.AUDIO_NOT_ACCESS = val
        elif arg == 'PIN_BUZZER':
            self.PIN_BUZZER = val
        elif arg == 'HOST':
            self.HOST = val
        elif arg == 'PORT':
            self.PORT = val
        elif arg == 'URL':
            self.URL = val
        elif arg == 'FUNCTION':
            self.FUNCTION = val
        elif arg == 'LAMP_CONNECT':
            self.LAMP_CONNECT = val
        elif arg == 'PIN_RELAY_NOT_ACCESS':
            self.LAMP_NOT_CONNECT = val
