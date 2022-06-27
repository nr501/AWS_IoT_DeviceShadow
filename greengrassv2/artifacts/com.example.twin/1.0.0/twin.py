import json
from random import randrange
import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    QOS,
    PublishToIoTCoreRequest
)
import sched, time
s = sched.scheduler(time.time, time.sleep)

TIMEOUT = 10
INTERVAL = 10

ipc_client = awsiot.greengrasscoreipc.connect()


def updateState(sc): 
    topic = "$aws/things/GreengrassVM-Benedikt/shadow/update"
    message_obj = {
        "state": {
            "reported": {
                "Temperatur": randrange(40),
                "Drehzahl": randrange(9000),
                "Lights": False
            }
        }
    }

    message = json.dumps(message_obj)
    qos = QOS.AT_LEAST_ONCE

    request = PublishToIoTCoreRequest()
    request.topic_name = topic
    request.payload = bytes(message, "utf-8")
    request.qos = qos
    operation = ipc_client.new_publish_to_iot_core()
    operation.activate(request)
    future = operation.get_response()
    future.result(TIMEOUT)
    sc.enter(INTERVAL, 1, updateState, (sc,))

s.enter(INTERVAL, 1, updateState, (s,))
s.run()