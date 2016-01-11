import time
import datetime
import os
import conjur
from conjur.config import config
import getpass


"""
def current_time(self):
    #current time
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')
    print st
"""
"""
def read_private_key(self):
    ## Reads the server.key
    text_file = open("/Users/keval/PycharmProjects/untitled1/server.key", "r")
    lines = text_file.read()
    print lines
"""


class conjur_lemur():
    def __init__(self):
         # building path
        config.appliance_url = "hti"
        config.account = "dev"
        config.cert_file = "/Users/" + getpass.getuser() + "/.conjur/conjur-dev.pem"
        self.conjurapi = conjur.new_from_netrc("/Users/" + getpass.getuser() + "/.netrc", config=config)
        print getpass.getuser()

    def write_privatekey_to_conjur(self,id_no, private_key, certificate_content):



        # creating a conjur variable and  storing a secret in the variable
        token = self.conjurapi.create_variable(
            id='dev/lemur/certs/' + id_no + '/key',
            value=private_key
        )
        print token.value()

        # creating a conjur variable and  storing a certificate in the variable
        token1 = self.conjurapi.create_variable(
            id='dev/lemur/certs/' + id_no + '/cert',
            value=certificate_content
        )
        print token1.value()



        # calling the function to show permissions and set new permissions
        variable_name = 'dev/lemur/certs/' + id_no + '/key'


    def read_privatekey_from_conjur(self,id_no):

        # checking the value written in the variable
        value = self.conjurapi.variable('dev/lemur/certs/' + id_no + '/key').value(version=None)
        return value

    def read_cert_from_conjur(self,id_no):

        value1 = self.conjurapi.variable('dev/lemur/certs/' + id_no + '/cert').value(version=None)
        return value1

    def set_conjur_permissions(self,conjur_variable):

        option = raw_input('Enter your option... r=read  e=execute   u=update ')
        print('you chose', option)

        if (option == 'r'):
            print "It shows all users/hosts that have (read) access to the variable"

            os.system("conjur resource permitted_roles variable:" + conjur_variable + " read")
        elif (option == 'e'):
            print "It shows all users/hosts that have (execute) access to the variable"

            os.system("conjur resource permitted_roles variable:" + conjur_variable + " read")
        elif (option == 'u'):
            print "It shows all users/hosts that have (update) access to the variable"

            os.system("conjur resource permitted_roles variable:" + conjur_variable + " read")
        else:
            print ("Enter a valid option from r, e, u")

        layer = 'dev/lemur/rw'
        variable_name = 'dev/lemur/certs/20150708_133534/key'
        privilige = raw_input('Enter what privilige you want to assign ... r=read  e=execute   u=update ')
        print('you chose', privilige)

        if (privilige == 'r'):

            os.system("conjur resource permit variable:" + conjur_variable + " layer:" + layer + " read")
        elif (privilige == 'e'):

            os.system("conjur resource permit variable:" + conjur_variable + " layer:" + layer + " read")
        elif (privilige == 'u'):

            os.system("conjur resource permit variable:" + conjur_variable + " layer:" + layer + " read")
        else:
            print ("Enter a valid option from r, e, u")


if __name__ == "__main__":
    # current time
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S')
    print st

    # reads the privatekey from a file
    text_file = open("/Users/keval/PycharmProjects/untitled1/server.key", "r")
    lines = text_file.read()
    print lines

    # reads the cert from a file
    text_file = open("/Users/keval/PycharmProjects/untitled1/server.crt", "r")
    crt = text_file.read()
    print crt

    conjurlemur = conjur_lemur()
    conjurlemur.write_privatekey_to_conjur(st, lines, crt)
    variable_name = 'dev/lemur/certs/' + st + '/key'
    x = conjurlemur.set_conjur_permissions(variable_name)
    print x
    y = conjurlemur.read_privatekey_from_conjur(st)
    print y
    z = conjurlemur.read_cert_from_conjur(st)
    print z