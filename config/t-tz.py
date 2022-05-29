
from datetime import datetime
import sys
import pytz
import json

output = {
    "datetime": datetime.now(pytz.timezone(sys.argv[1])).strftime('%a %b %d, %I:%M%p'),
    "timezone": sys.argv[1]
}
print(json.dumps(output))