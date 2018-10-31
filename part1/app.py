from flask import Flask
from redis import Redis, RedisError
import os
import redis
import socket


# Connect to Redis
rcon = redis.StrictRedis(host="redis-server", db=0, decode_responses=True)

app = Flask(__name__)


@app.route("/")
def redis_counter():
    try:
        visits = rcon.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"


    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3010)
