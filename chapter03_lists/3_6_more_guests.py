guests = ['raili', 'juha', 'ronja']
message = "I'd like to invite you to dinner"
print(f'{message}, {guests[0].title()}!')
print(f'{message}, {guests[1].title()}!')
print(f'{message}, {guests[2].title()}!')
print(f"Sadly, {guests[2].title()} can't make it!")
guests[2] = 'laura'
print(f'{message}, {guests[2].title()}!')
print('There will be more guests attending!')
guests.insert(3, 'harri')
guests.insert(4, 'henri')
guests.insert(5, 'arto')
print(f'{message}, {guests[3].title()}!')
print(f'{message}, {guests[4].title()}!')
print(f'{message}, {guests[5].title()}!')
