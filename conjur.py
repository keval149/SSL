import time
import datetime
import os
import conjur
from conjur.config import config
import getpass
import terminal
from terminal import permission_allowed
from terminal import grant_permission

#current time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')
print st

## Reads the server.key
text_file = open("/Users/keval/PycharmProjects/untitled1/server.key", "r")
lines = text_file.read()
print lines


config.appliance_url = "https://conjur-/api"
config.account = "dev"
config.cert_file = "/Users/" + getpass.getuser() + "/.conjur/conjur-dev.pem"

conjurapi = conjur.new_from_netrc("/Users/" + getpass.getuser() + "/.netrc", config=config)

print getpass.getuser()
# create a variable to store a secret


token = conjurapi.create_variable(
    id='dev/lemur/certs/' + st + '/key',
    value=lines
)
print token.value()

value = conjurapi.variable('dev/lemur/certs/' + st + '/key').value(version=None)
print value


permit = permission_allowed()

grant = grant_permission()


