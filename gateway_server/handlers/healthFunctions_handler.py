from health.healthFunctions import *
from models.Health import *

async def health_handler(start_time):
    ready_report = await readyCheck(start_time)
    alive_report = await liveCheck(start_time)
    
    healthReport = Health(
        checks=[ready_report, alive_report]
    )
    return healthReport
