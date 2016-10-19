def search(arg, Contacts, session):
	"Function to search for contact in a Contacts"
	search_results = []
	count = 1
	for instance in session.query(Contacts):
		if arg['<name>'] == instance.name:
			search_results.append({'count': count, 'name':instance.name, 'second_name':instance.second_name, 'Phone number':instance.phone_number})
			count+=1

        while True:

			if count == 1:
				return (count, "%s is not in your contacts " %(arg['<name>']))

			if count == 2:
				return (count, "Name: %s %s, Number: %s" %(arg['<name>'], search_results[0]['second_name'], search_results[0]["Phone number"]), search_results[0]["Phone number"])
			

			print "Which %s?" %(arg['<name>'])
			for result in search_results:
				print "[%d]  %s %s" % (result['count'], result['name'], result['second_name'])

			option_selected = input('Enter the corresponding number: ')
			if isinstance (option_selected,int):
				for result in search_results:
					if option_selected == result['count']:
						return ( 2, "Name: %s %s, Number: %s" % (result['name'], result['second_name'], result['Phone number']), result['Phone number'])
					
			else:
				print "Please select one of the Options"

	return "Check code something is not right"