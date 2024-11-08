from datetime import datetime
import time
from models.Health import CheckData, ServiceCheck, GeneralCheck, Health
from communication.communication import verifyConnection

async def readyCheck(start_time):
    nats_status = await checkReadyCommunication()
    nats_status_label = "READY" if nats_status else "DOWN"
    check_status = "UP" if nats_status else "DOWN"
    
    checkReport = ServiceCheck(
        data=CheckData(
            from_=datetime.utcnow().isoformat(),
            status=nats_status_label
        ),
        name="Communication Ready connection check.",
        status=check_status
    )
    
    general_status = "UP" if nats_status else "DOWN"
    uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
    version = "1.0.0"
    
    report = GeneralCheck(
        status=general_status,
        checks=[checkReport],
        version=version,
        uptime=uptime
    )
    return report

async def liveCheck(start_time):
    nats_status = await checkLiveCommunication()
    nats_status_label = "LIVE" if nats_status else "DOWN"
    check_status = "UP" if nats_status else "DOWN"
    
    checkReport = ServiceCheck(
        data=CheckData(
            from_=datetime.utcnow().isoformat(),
            status=nats_status_label
        ),
        name="Communication Live connection check.",
        status=check_status
    )

    general_status = "UP" if nats_status else "DOWN"
    uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
    version = "1.0.0"
    
    report = GeneralCheck(
        status=general_status,
        checks=[checkReport],
        version=version,
        uptime=uptime
    )
    return report

async def checkReadyCommunication():
    try:
        return await verifyConnection()
    except Exception:
        return False

async def checkLiveCommunication():
    try:
        return await verifyConnection()
    except Exception:
        return False
