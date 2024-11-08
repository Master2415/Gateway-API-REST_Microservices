from datetime import datetime
import time

class CheckData:
    def __init__(self, from_, status):
        self.from_ = from_
        self.status = status

    def to_dict(self):
        return {
            "from": self.from_,
            "status": self.status
        }

class ServiceCheck:
    def __init__(self, data, name, status):
        self.data = data
        self.name = name
        self.status = status

    def to_dict(self):
        return {
            "data": self.data.to_dict(),
            "name": self.name,
            "status": self.status
        }

class GeneralCheck:
    def __init__(self, status, checks, version, uptime):
        self.status = status
        self.checks = checks
        self.version = version
        self.uptime = uptime

    def to_dict(self):
        return {
            "status": self.status,
            "checks": [check.to_dict() for check in self.checks],
            "version": self.version,
            "uptime": self.uptime
        }

class Health:
    def __init__(self, checks):
        self.checks = checks

    def to_dict(self):
        return {
            "checks": [check.to_dict() for check in self.checks]
        }
