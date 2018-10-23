import plotly.offline as offline
import plotly.graph_objs as go
def report(name,x1,x2,x3,y1,y2,y3):
    trace0 = go.Bar(
                x=[x1], name=x1,
                y=[y1],
                text=x1,hoverinfo='text',
    marker=dict(color='green'),width=[0.3])
    trace1 = go.Bar(
                x=[x2], name=x2,
                y=[y2],
                text=x2,hoverinfo='text',
    marker=dict(color='red'),width=[0.3])
    trace3 = go.Bar(
                x=[x3], name=x3,
                y=[y3],
                text=x3,hoverinfo='text',
    marker=dict(color='black'),width=[0.3])
    data=[trace0,trace1,trace3]
    layout=go.Layout(title=name+" "+"GRAPH FOR THE TEST CASE EXECUTED",titlefont=dict(size=18,family='Arial'),font=dict(family='Arial',size=14),xaxis=dict(title='TEST CASE RESULTS',titlefont=dict(family='Arial',size=16,color='grey'),showticklabels=True,tickfont=dict(family='Old Standart TT',size=14,color='black')))
    fig=go.Figure(data=data,layout=layout)

    offline.plot(fig,filename= 'STATUS.html',image='png',image_height=600,image_width=400)
    return 0
