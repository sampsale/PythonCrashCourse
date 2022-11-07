guests = ['raili', 'juha', 'ronja']
message = "I'd like to invite you to dinner"
print(f'{message}, {guests[0].title()}!')
print(f'{message}, {guests[1].title()}!')
print(f"Sadly, {guests[2].title()} can't make it !")
guests[2] = 'laura'
print(f'{message}, {guests[2].title()}!')