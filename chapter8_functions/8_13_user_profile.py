def build_profile(f_name, l_name, **user_info):
    user_info['first_name'] = f_name
    user_info['last_name'] = l_name
    return user_info


user_profile = build_profile(
    'Sampsa', 'Leikas', location='Helsinki', field='ICT', age=27)


for key, value in user_profile.items():
    print(F"\t{key.title()}: {value}")
