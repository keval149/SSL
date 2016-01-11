import os
def permission_allowed():
    option = raw_input('Enter your option... r=read  e=execute   u=update ')
    print('you chose', option)
    variable_name = 'dev/lemur/certs/20150708_133534/key'

    if (option == 'r'):
        print "It shows all users/hosts that have (read) access to the variable"
        #print "you are in read"
        #variable_name = 'dev/lemur/certs/20150708_133534/key'
        os.system("conjur resource permitted_roles variable:"+variable_name+" read")
    elif (option == 'e'):
        print "It shows all users/hosts that have (execute) access to the variable"
        #print "you are in execute"
        #variable_name = 'dev/lemur/certs/20150708_133534/key'
        os.system("conjur resource permitted_roles variable:"+variable_name+" read")
    elif (option == 'u'):
        print "It shows all users/hosts that have (update) access to the variable"
        #print "you are in update"
        #variable_name = 'dev/lemur/certs/20150708_133534/key'
        os.system("conjur resource permitted_roles variable:"+variable_name+" read")
    else:
        print ("Enter a valid option from r, e, u")



    # grant read permission on the variable to the layer
    #conjur resource permit variable:dev/lemur/certs/20150708_133534/key layer:dev/lemur/rw read

# to grant permission to a variable to rea execute or update
def grant_permission():
    layer = 'dev/lemur/rw'
    variable_name = 'dev/lemur/certs/20150708_133534/key'
    privilige = raw_input('Enter what privilige you want to assign ... r=read  e=execute   u=update ')
    print('you chose', privilige)

    if (privilige == 'r'):
        #print "It shows all users/hosts that have (read) access to the variable"
        #print "you are providing read acces"
        #variable_name = 'dev/lemur/certs/20150708_133534/key'
        os.system("conjur resource permit variable:"+variable_name+" layer:"+layer+" read")
    elif (privilige == 'e'):
        #print "It shows all users/hosts that have (execute) access to the variable"
        #print "you are access to execute"
        #variable_name = 'dev/lemur/certs/20150708_133534/key'
        os.system("conjur resource permit variable:"+variable_name+" layer:"+layer+" read")
    elif (privilige == 'u'):
        #print "It shows all users/hosts that have (update) access to the variable"
        #print "you are access to update"
        #variable_name = 'dev/lemur/certs/20150708_133534/key'
        os.system("conjur resource permit variable:"+variable_name+" layer:"+layer+" read")
    else:
        print ("Enter a valid option from r, e, u")


"""
variable_name = 'dev/lemur/certs/20150708_133534/key'
layer = 'dev/lemur/rw'

permit = permission_allowed()

grant = grant_permission()
"""