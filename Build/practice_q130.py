#Q:Write a Python program that uses double quotes to display strings.

import json

data = {'Alex': 1, 'Suresh': 2,'Agness': 3}

json_string = json.dumps(data)
print(json_string)