from randomwalk import RandomWalk
import plotly.express as px


# random walk with 5000 steps
rw = RandomWalk(5000)
rw.fill_walk()

# plot RW as line chart with plotly
fig = px.line(x=rw.x_values, y=rw.y_values)
# add start and end points
fig.add_scatter(x=[0], y=[0], name="Start point", line=dict(color='green'))
fig.add_scatter(x=[rw.x_values[-1]], y=[rw.y_values[-1]], name="End point", line=dict(color='red'))
# update scatter marker size and border line
fig.update_traces(marker=dict(size=15,
                              line=dict(width=2,
                                        color='DarkSlateGrey')))
fig.show()