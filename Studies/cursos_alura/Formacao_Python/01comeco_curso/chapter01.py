
users = [
	{"id": 0, "name": "Hero"},
	{"id": 1, "name": "Dunn"},
	{"id": 2, "name": "Sue"},
	{"id": 3, "name": "Chi"},
	{"id": 4, "name": "Thor"},
	{"id": 5, "name": "Clive"},
	{"id": 6, "name": "Hicks"},
	{"id": 7, "name": "Devin"},
	{"id": 8, "name": "Kate"},
	{"id": 9, "name": "Klein"}
]

friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

#initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

#and loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
	friendships[i].append(j) # add j as a friend of user i
	friendships[j].append(i) # add i as a friend of user j

def number_of_friends(user):
	#how many friends does user have?
	user_id = user["id"]
	friend_ids = friendships[user_id]
	return len(friend_ids)

total_connections = sum(number_of_friends(user)
							for user in users)
#print(total_connections) OK

num_users = len(users)
avg_connections = total_connections / num_users

#create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(
	key=lambda id_and_friends: id_and_friends[1],
	reverse=True)

print(num_friends_by_id)

def foaf_ids_bad(user):
	"""foaf is short for 'friend of a friend'"""
	return [foaf_id
			for friend_id in friendships[user["id"]]
			for foaf_id in friendships[friend_id]]

#print(foaf_ids_bad(users[0])) OK

print(friendships[0])
print(friendships[1])
print(friendships[2])

from collections import Counter # not loaded by default

def friends_of_friends(user):	
	user_id = user["id"]
	return Counter(
		foaf_id
		for friend_id in friendships[user_id]	#For each of my friends,
		for foaf_id in friendships[friend_id]	# find their friends
		if foaf_id != user_id					# who aren't me
		and foaf_id not in friendships[user_id] # and aren't my friends.
	)

print(friends_of_friends(users[3])) 			#Counter({0: 2, 5: 1})