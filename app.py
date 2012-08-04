grab incoming text info (body = zip code)

def toomany():
	find closest 3
	ask if they want to see more
		send the next 3

def decideSend(starting zip code):
	retrieve matches
	if 1-3?
		return it
	if too many
		toomany()
	if none
		get next nearest
		decideSend(next nearest)

reply to user with info