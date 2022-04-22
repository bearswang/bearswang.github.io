#!/user/bin/env python3

import os
import subprocess as sp

sp.run(['python jemdoc.py index.jemdoc'], shell=True)
sp.run(['python jemdoc.py research.jemdoc'], shell=True)
sp.run(['python jemdoc.py software.jemdoc'], shell=True)
sp.run(['python jemdoc.py publications.jemdoc'], shell=True)
sp.run(['python jemdoc.py teaching.jemdoc'], shell=True)
sp.run(['python jemdoc.py demo.jemdoc'], shell=True)
sp.run(['python jemdoc.py group.jemdoc'], shell=True)