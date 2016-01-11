# test script for LDAP auth/query


import ldap
import getpass

# sAMAccountName contains username

if __name__ == "__main__":
    ldap_server="ldap server name"
    username = input("Enter LDAP username: ")
    password= getpass.getpass("Enter LDAP password for " + username + "\n")
    
    # the following is the user_dn format provided by the ldap server
    user_dn = "CN=" + username + ",ou=****,ou=****,dc=**,dc=****,dc=*******,dc=com"
    
    # adjust this to your base dn for searching
    base_dn = "ou=****,ou=****,dc=**,dc=****,dc=*******,dc=com"
    
    connect = ldap.initialize("ldap://" + ldap_server + ":389")
    
    search_filter = "CN=" + username
    
    try:
        #if authentication successful, get the full user data
        #connect.bind_s(user_dn,password)
        connect.simple_bind_s(user_dn,password)
        #result = connect.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)

        print "successfully authenticated!"
        # return all user data results
        connect.unbind_s()
        #print result
    except ldap.LDAPError:

        connect.unbind_s()
        print "authentication error"
    