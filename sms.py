# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
# Specify your login credentials
def text(receiving_number, message):
	username = "kevinoluoch"
	apikey   = "4fa7ca9b35ecc411875512ee24c42318b756d6cff5c575d4dca73e8b686e1974"

	receiving_number = "+" + str(receiving_number)
	#to      = "+254711835117"
	# Create a new instance of our awesome gateway class
	gateway = AfricasTalkingGateway(username, apikey)

    # Any gateway errors will be captured by our custom Exception class below, 
    # so wrap the call in a try-catch block
	try:
		results = gateway.sendMessage(receiving_number, message)

	except AfricasTalkingGatewayException, e:
		print 'Encountered an error while sending: %s' % str(e)

	return results