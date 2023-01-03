import requests
from plotly.graph_objs import Bar
from plotly import offline



def sortData():
    r = fetchData()
    # get json of results
    response_dict = r.json()
    # get items 
    repo_dicts = response_dict['items']
    # init lists for name, stars and labels
    repo_names, stars, labels = [], [], []


    for repo in repo_dicts:
        # name is a-element with link
        link = f"<a href={repo['url']}>{repo['name']}</a>"
        repo_names.append(link)
        
        stars.append(repo['stargazers_count'])

        # description has owner and description
        owner = repo['owner']['login']
        description = repo['description']
        labels.append(f"{owner}<br />{description}")
    plotGraph(repo_names, stars, labels)

def plotGraph(repo_names, stars, labels):
    # init data
    data = [{
        'type': 'bar',
        'x': repo_names,
        'y': stars,
        'hovertext': labels
    }]

    # layout 
    my_layout = {
        'title': 'Top JS repos on GitHub by stars',
        'xaxis': {'title': 'Repo'},
        'yaxis': {'title': 'Stars'}
    }

    # plot
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='JS_repos.html')

def fetchData():
    # get most popular JS repos on GH and sort by number of stars (this query will run for too long and results will be incomplete)
    url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
    # use v3 
    headers = {'Accept': 'application/vnd.github.v3+json'}
    # get data
    r = requests.get(url, headers=headers)
    return r


if __name__ == '__main__':
    sortData()
