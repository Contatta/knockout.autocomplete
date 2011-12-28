#!/usr/bin/env python

import httplib
import urllib
import sys
import os


dir_repo = os.path.dirname(os.path.abspath(__file__))

file_src = os.path.join(dir_repo, 'knockout.autocomplete.js')
file_min = os.path.join(dir_repo, 'knockout.autocomplete.min.js')


contents = None
with open(file_src) as f:
  contents = f.read()


params = urllib.urlencode([
  ('js_code', contents),
  ('compilation_level', 'SIMPLE_OPTIMIZATIONS'),
  ('output_format', 'text'),
  ('output_info', 'compiled_code'),
])

headers = { "Content-type": "application/x-www-form-urlencoded" }
conn = httplib.HTTPConnection('closure-compiler.appspot.com')
conn.request('POST', '/compile', params, headers)
response = conn.getresponse()
data = response.read()
conn.close()


with open(file_min, 'w') as f:
  f.write(data)
