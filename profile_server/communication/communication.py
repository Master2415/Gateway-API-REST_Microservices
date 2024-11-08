import os
import nats
import json
import asyncio
from nats.aio.client import Client as NATS
import logging

class NATSClient:
    def __init__(self):
        self.nc = NATS()
        self._is_connected = False

    async def connect(self):
        if not self._is_connected:
            nats_hosts = os.getenv("PS_NATS_SERVER", "localhost")
            nats_url = f"nats://{nats_hosts}:4222"
            try:
                await asyncio.wait_for(self.nc.connect(nats_url), timeout=1)
                self._is_connected = True
            except (Exception, asyncio.TimeoutError) as e:
                logging.error(f"Failed to connect to NATS: {e}")
                self._is_connected = False

    async def close(self):
        if self._is_connected:
            await self.nc.close()
            self._is_connected = False

async def verifyCommunication():
    nc = NATSClient()
    await nc.connect()

    if nc._is_connected:
        log_dict = {
            "app_name": "empty",
            "log_type": "empty",
            "module": "empty",
            "log_date_time": "empty",
            "summary": "empty",
            "description": "empty"
        }

        log_json = json.dumps(log_dict)
        try:
            await nc.nc.publish("empty", log_json.encode())
            await nc.nc.drain()
            return True
        except Exception as e:
            logging.error(f"Failed to send message: {e}")
        finally:
            await nc.close()
    return False


async def sendLog(log):
    try:
        log_dict = {
            "app_name": log.app_name,
            "log_type": log.log_type,
            "module": log.module,
            "log_date_time": log.log_date_time,
            "summary": log.summary,
            "description": log.description
        }

        log_json = json.dumps(log_dict)

        nc = await nats.connect("nats://localhost:4222")
        await nc.publish("ProfilesServer", log_json.encode())
        await nc.flush()
        await nc.close()
        print("Log sended.")
    except Exception as e:
        print("Error:", e)
