class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass
    def __init__(self):
        self.account_sid = 'AC90d0da15a4e51801a75729a6d3e75781'
 	    self.auth_token = os.environ.get("AUTH_TOKEN")
        self.client = Client(account_sic, auth_token)    
        self.ToPhone = "+15593009564"
        self.fromPhone = "+18302754848"




# def sendMessage(list_of_articles, percentage):
# 	account_sid = 'AC90d0da15a4e51801a75729a6d3e75781'
# 	auth_token = os.environ.get("AUTH_TOKEN")
# 	client = Client(account_sid, auth_token)
	
# 	if percentage >= 0:
# 		print(type(list_of_articles))
# 	for article in list_of_articles:
# 		title=article["title"]
# 		description=article["description"]
# 		if percentage > 5:
# 			message = client.messages.create(
# 								body=f"\n{STOCK}:🔺{percentage}%\n\nHeadline:{title}\n\nBrief:{description}",
# 								from_='+18302754848',
# 								to='+15593009564',
# 								)
# 		elif percentage < -5:
# 			message = client.messages.create(
# 								body=f"\n{STOCK}:🔻{percentage}%\n\nHeadline:{title}\n\nBrief:{description}",
# 								from_='+18302754848',
# 								to='+15593009564',
# 								)
