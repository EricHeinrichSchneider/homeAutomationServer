from datetime import timedelta
import os

class serverUtil:
    def getServerTime(self):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            delta = timedelta(seconds = uptime_seconds)
            retString  = str(delta.days).zfill(3) + ":"
            retString += str(delta.seconds//3600).zfill(2) + ":"
            retString += str((delta.seconds//60)%60).zfill(2) + ":"
            retString += str(delta.seconds % 60).zfill(2) +":"
            retString += str(delta.microseconds)
            return retString
        return None

    def getLoadAvg(self):
        sysload = None
        try:
            sysload = os.getloadavg()
        except OSError as e:
            sysload = None
        return sysload
