from datetime import datetime
import time
from models.Health import CheckData, ServiceCheck, GeneralCheck, Health
from communication.communication import verifyCommunication
from database.connection import verifyDatabase

async def readyCheck(start_time):
    nats_status = await checkReadyCommunication()
    nats_status_label = "READY" if nats_status else "DOWN"
    check_communication_status = "UP" if nats_status else "DOWN"
    
    check_communication_Report = ServiceCheck(
        data=CheckData(
            from_=datetime.utcnow().isoformat(),
            status=nats_status_label
        ),
        name="Communication Ready connection check.",
        status=check_communication_status
    )

    database_status = await checkReadyDatabase()
    database_status_label = "READY" if database_status else "DOWN"
    check_database_status = "UP" if database_status else "DOWN"
    
    check_database_Report = ServiceCheck(
        data=CheckData(
            from_=datetime.utcnow().isoformat(),
            status=database_status_label
        ),
        name="Database Ready connection check.",
        status=check_database_status
    )
    
    general_status = "UP" if nats_status and database_status else "DOWN"
    uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
    version = "1.0.0"
    
    report = GeneralCheck(
        status=general_status,
        checks=[check_communication_Report, check_database_Report],
        version=version,
        uptime=uptime
    )
    return report

async def liveCheck(start_time):
    nats_status = await checkLiveCommunication()
    nats_status_label = "LIVE" if nats_status else "DOWN"
    check_communication_status = "UP" if nats_status else "DOWN"
    
    check_communication_Report = ServiceCheck(
        data=CheckData(
            from_=datetime.utcnow().isoformat(),
            status=nats_status_label
        ),
        name="Communication Live connection check.",
        status=check_communication_status
    )

    database_status = await checkLiveDatabase()
    database_status_label = "LIVE" if database_status else "DOWN"
    check_database_status = "UP" if database_status else "DOWN"
    
    check_database_Report = ServiceCheck(
        data=CheckData(
            from_=datetime.utcnow().isoformat(),
            status=database_status_label
        ),
        name="Database Live connection check.",
        status=check_database_status
    )

    general_status = "UP" if nats_status and database_status else "DOWN"
    uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
    version = "1.0.0"
    
    report = GeneralCheck(
        status=general_status,
        checks=[check_communication_Report, check_database_Report],
        version=version,
        uptime=uptime
    )
    return report

async def checkReadyCommunication():
    try:
        return await verifyCommunication()
    except Exception:
        return False

async def checkLiveCommunication():
    try:
        return await verifyCommunication()
    except Exception:
        return False

async def checkReadyDatabase():
    try:
        return await verifyDatabase()
    except Exception:
        return False

async def checkLiveDatabase():
    try:
        return await verifyDatabase()
    except Exception:
        return False
