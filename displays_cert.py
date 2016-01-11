import requests
from requests.auth import HTTPBasicAuth
import json

# Retrieving a Certificate
auth = HTTPBasicAuth("acc no","api key")


head = {'Content-Type': 'application/vnd.digicert.rest-v1+json'}
def Retrieve_Issued_Certificate(ord_id):

    url1 = "https://api.digicert.com/order/"+ord_id+"/certificate"

    orderid = requests.get(url1, auth = auth, headers= head).json()["order_id"]
    print ("order_id is:")
    print orderid

    serial = requests.get(url1, auth = auth, headers= head).json()["serial"]
    print ("serial is:")
    print serial

    certificate = requests.get(url1, auth = auth, headers= head).json()["certs"]["certificate"]
    print ("certificate is:")
    print certificate
    #write(ord_id,count)
    #count = count + 1

    intermediate = requests.get(url1, auth = auth, headers= head).json()["certs"]["intermediate"]
    print ("intermediate is:")
    print intermediate
    #write(ord_id,count)
    #count = count + 1

    root = requests.get(url1, auth = auth, headers= head).json()["certs"]["root"]
    print ("root is:")
    print root
    #write(ord_id,count)
    #count = count + 1

    pkcs7 = requests.get(url1, auth = auth, headers= head).json()["certs"]["pkcs7"]
    print ("pkcs7 is:")
    print pkcs7
    #write(ord_id,count)

    return certificate,intermediate,root,pkcs7,orderid

def View_order_details(ord_id):
    # get order details
    url = "https://api.digicert.com/order/"+ord_id
    print ("Viewing the Order Details")
    details = requests.get(url,auth=auth).text
    print ("details are:")
    print details

    details_order_id =  requests.get(url,auth=auth).json()["certificate_details"]["order_id"]
    print ("details_order_id is:")
    print details_order_id

    status =  requests.get(url,auth=auth).json()["certificate_details"]["status"]
    print ("status is:")
    print status

    product_name =  requests.get(url,auth=auth).json()["certificate_details"]["product_name"]
    print ("product_name is:")
    print product_name

    validity =  requests.get(url,auth=auth).json()["certificate_details"]["validity"]
    print ("validity is:")
    print validity

    org_unit =  requests.get(url,auth=auth).json()["certificate_details"]["org_unit"]
    print ("org_unit is:")
    print org_unit

    business_unit =  requests.get(url,auth=auth).json()["certificate_details"]["business_unit"]
    print ("business_unit is:")
    print business_unit

    common_name =  requests.get(url,auth=auth).json()["certificate_details"]["common_name"]
    print ("common_name is:")
    print common_name

    sans =  requests.get(url,auth=auth).json()["certificate_details"]["sans"]
    print ("sans is:")
    print sans

    org_unit =  requests.get(url,auth=auth).json()["certificate_details"]["org_unit"]
    print ("org_unit is:")
    print org_unit

    valid_from =  requests.get(url,auth=auth).json()["certificate_details"]["valid_from"]
    print ("valid_from is:")
    print valid_from

    valid_till =  requests.get(url,auth=auth).json()["certificate_details"]["valid_till"]
    print ("valid_till is:")
    print valid_till

    site_seal_token =  requests.get(url,auth=auth).json()["certificate_details"]["site_seal_token"]
    print ("site_seal_token is:")
    print site_seal_token

    server_type =  requests.get(url,auth=auth).json()["certificate_details"]["server_type"]
    print ("server_type is:")
    print server_type

    server_type_name =  requests.get(url,auth=auth).json()["certificate_details"]["server_type_name"]
    print ("server_type_name is:")
    print server_type_name

    order_total =  requests.get(url,auth=auth).json()["receipt"]["order_total"]
    print ("order_total is:")
    print order_total
    #####################

