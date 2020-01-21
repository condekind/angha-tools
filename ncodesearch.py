#!/usr/bin/python3
import sys
import json
from random import randrange

src = ''.join(sys.stdin.readlines())

names = ['alice', 'bob', 'clodoveu', 'death', 'ecstasy']
paths = ['/path/to/' + x for x in names]
features = [{
		'numOfMul': randrange(69),
		'numOfLoops': randrange(666),
		'numOfEdges': randrange(420),
	} for _ in names ]
content = [{'code': '{}'.format(src)} for _ in names]

suites = [{
	'benchName': names.pop(),
	'path': paths.pop(),
	'features': features.pop(),
	'content': content.pop(),
	}
	for _ in names ]

print(json.dumps(suites))
