from AzureDB import AzureDB

# AzureDB().azureAddData()
# AzureDB().azureDeleteData()

with AzureDB() as a:
    data = a.azureGetData()
    for result in data:
        print("%snapisał: \"%s\"" % (result['nick'], result['text'], result['createdDate']))
