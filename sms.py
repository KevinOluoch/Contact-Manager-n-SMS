# Originally copied from
# Edited to fit its purpose in the code
# Importing the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException


def text(receiving_number, message):
	"""
	This function takes a phone number and message as input,
	then attempts to send the message to the given number.
	It then returns feedback on the attempt.
	This could be:
	              Success: in sendin the message,
	              Invalid Phone Number: if number doesn't exist or is wrongly formatted
	              No Internet connection"""


    # The login credentials
	username = "kevinoluoch"
	apikey = "4fa7ca9b35ecc411875512ee24c42318b756d6cff5c575d4dca73e8b686e1974"

    # The number receiving the text is prefixed with a +
	receiving_number = "+" + str(receiving_number)
	
	# Creating a new instance of the gateway class in AfricasTalkingGateway
	gateway = AfricasTalkingGateway(username, apikey)

    # Any gateway errors will be captured by the custom Exception class in AfricasTalkingGateway , 
	try:
		results = gateway.sendMessage(receiving_number, message,)

	except AfricasTalkingGatewayException, e: 
		results = [{'status' : 'Encountered an error while sending: %s' % str(e)}]

	except: # Captures internet connection error
	    results = [{'status' : "Message Not Sent: No internet connection"}]

	return results