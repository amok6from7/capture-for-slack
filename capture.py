# -*- coding: utf-8 -*-

import commands
import datetime

now = datetime.datetime.now()
fmt_name = "{0:%Y%m%d-%H%M%S}.jpg".format(now)

commands.getoutput("raspistill -w 1200 -h 900 -o " + fmt_name + " -ev 3 -ISO 800")

from slacker import Slacker
token = "input-slack-token"
slacker = Slacker(token)
channel_name = "#" + "camera"
result = slacker.files.upload(fmt_name,channels=['channel-name'])
slacker.pins.add(channel='channel-name', file_=result.body['file']['id'])
