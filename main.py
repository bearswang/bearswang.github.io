#!/user/bin/env python3
import os
import subprocess as sp

sp.run(['bash', '-c', 'python2 jemdoc.py index.jemdoc'])
sp.run(['bash', '-c', 'python2 jemdoc.py research.jemdoc'])
sp.run(['bash', '-c', 'python2 jemdoc.py software.jemdoc'])
sp.run(['bash', '-c', 'python2 jemdoc.py publications.jemdoc'])
sp.run(['bash', '-c', 'python2 jemdoc.py teaching.jemdoc'])