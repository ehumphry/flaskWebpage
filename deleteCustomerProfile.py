import os, sys
#import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
#constants = imp.load_source('modulename', 'constants.py')

def deleteCustomerProfile(customerProfileId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = '4urP8Y47'
    merchantAuth.transactionKey = '538g4Tg2uMBte3W8' 

    deleteCustomerProfile = apicontractsv1.deleteCustomerProfileRequest()
    deleteCustomerProfile.merchantAuthentication = merchantAuth
    deleteCustomerProfile.customerProfileId = customerProfileId

    controller = deleteCustomerProfileController(deleteCustomerProfile)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print("Successfully deleted customer with customer profile id %s" % deleteCustomerProfile.customerProfileId)
    else:
        print(response.messages.message[0]['text'].text)
        print("Failed to delete customer profile with customer profile id %s" % deleteCustomerProfile.customerProfileId)

    return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    deleteCustomerProfile(constants.customerProfileId)