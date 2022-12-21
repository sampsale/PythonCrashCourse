import os

# script to create folders, because why not
folder_names = ['sitka_rainfall', 'sitka-death_valley_comparision', 'san_francisco',
                'refactoring', 'explore', 'refactoring', 'earthquakes_30_days', 'recent_earthquakes', 'world_fires']

for index, assignment in enumerate(folder_names):
    try:
        # skip if assignment is about refactoring previous assignments (no separate file for these)
        if assignment != 'refactoring':
            # add 0 if less that 2 digits 
            directory = f'16_{"%02d" % (index+1,)}_{folder_names[index]}'
            os.mkdir(directory)
            # make subdirectories for data because why not
            os.makedirs(os.path.join(directory, 'data'))
            # make python files 
            fp = open(f'{directory}/{assignment}.py', 'x')
    # if already exists, pass
    except FileExistsError:
        print(f"\t{assignment} directory already exists")

