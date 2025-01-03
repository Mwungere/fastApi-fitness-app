import os
from random import randint

# Define varying commit intensities for each day (0 to 10 commits per day)
for i in reversed(range(10)):  # Last 10 days
    commits_today = randint(1, 20)  # Random number of commits for the day (1 to 20)
    for _ in range(commits_today):
        d = str(i) + ' days ago'  # Fake commit date
        # Modify the file to simulate a change
        with open('file.txt', 'a') as file:
            file.write(d + '\n')  # Write the date into the file
        # Stage and commit the changes with a fake date
        os.system(f'git add .')
        os.system(f'git commit --date="{d}" -m "Automated commit for {d}"')

# Push all changes to the repository
os.system('git push -u origin main')
