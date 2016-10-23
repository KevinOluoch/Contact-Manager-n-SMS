def search(arg, Contacts, session):
	"""
	A function to search for a given entry in a Contacts,
	given the first name of the contact as input.
	"""


	search_results = []
	count = 1
	# Searching for all entries matching the request name and storing them in a list
	for entry in session.query(Contacts):
		if arg['<name>'] == entry.name or arg['<name>'] == entry.second_name:
			search_results.append({
				                   'count' : count, 'name' : entry.name,
			                       'second_name' : entry.second_name,
			                       'Phone number' : entry.phone_number})
			count+=1
        
        while True:
            # Gives feedback if requested name is not in contacts
			if count == 1:
				return (count, "%s is not in your contacts " %(arg['<name>']))
            # Gives feedback if requested name is found in contacts
			if count == 2:
				return (
					    count, "Name: %s %s, Number: %s" %(arg['<name>'],
				        search_results[0]['second_name'],
				        search_results[0]["Phone number"]),
				        search_results[0]["Phone number"])
			
            # Gives options if requested name appears several times in contacts
			print "Which %s?" %(arg['<name>'])
			for result in search_results:
				print "[%d]  %s %s" % (result['count'], result['name'],
				                       result['second_name'])
            # The user then chooses one option
			option_selected = raw_input('Enter the corresponding number: ')
			if option_selected.isdigit():
				option_selected = int(option_selected)
				# Option is retrieved from results and then returned
				for result in search_results:
					if option_selected == result['count']:
						return ( 
							    2, "Name: %s %s, Number: %s" %(result['name'],
						        result['second_name'], result['Phone number']),
						        result['Phone number'])
					
			else:
				print "Please select one of the Options"

				