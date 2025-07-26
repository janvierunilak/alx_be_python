users={'Gad':'Active','Mutamba ':'Inactive','Kanoni':'Active','Mugeshi':'Inactive','Janvier':'Active'}
for user,status in users.copy().items():
    print(user,status)
    if status=='Inactive':
        del users[user]
active_users={}
for user,status in users.items():
    if status=='Active':
        active_users[user]=status
        print(active_users)


        
            
