

import requests
from plotly.graph_objs import Bar
from plotly import offline
from operator import itemgetter

# get hacker news top stories
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
submission_ids = r.json()

# init list
submissions = []

# loop thorough first top 30 news
for submission_id in submission_ids[:30]:
    # fetch comments and data for the submission in question
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()
    # use try-except, because there is some inconsistensies there
    try: 
        # get title, link and number of comments into dictionary
        submission_dict = {
            'title': response_dict['title'],
            'comments': response_dict['descendants']
        }
        # append into submissions list
        submissions.append(submission_dict)
    except: 
        print(f"Error occured with {submission_id}")

# sort by number of comments
submissions = sorted(submissions, key=itemgetter('comments'), reverse=True)

### MAKE BARCHART OF TOP STORIES
# init data
data = [{
    'type': 'bar',
    # use list comprehension to get title and comments for axis
    'x': [submission_dict['title'] for submission_dict in submissions],
    'y': [submission_dict['comments'] for submission_dict in submissions],
}]

# layout 
my_layout = {
    'title': 'Top articles on HackerNews sorted by comments',
    'xaxis': {'title': 'Article'},
    'yaxis': {'title': 'Comments'}
}

# plot
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hackernews_articles.html')