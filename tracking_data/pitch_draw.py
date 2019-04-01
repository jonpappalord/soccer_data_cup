"""

functions for data visualizations of tracking data

"""

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np



pitch_layout = dict( hovermode='closest', autosize=False,
                                    width=550,
                                    height=400,
                                    plot_bgcolor='rgb(59,205,55)',
                                    xaxis={
                                        'range': [0, 100],
                                        'showgrid': False,
                                        'showticklabels': True,
                                    },
                                    yaxis={
                                        'range': [0, 100],
                                        'showgrid': False,
                                        'showticklabels': True,
                                    },
                                    shapes=[
                                        {
                                            'type': 'circle',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 35,
                                            'x0': 40,
                                            'y1': 65,
                                            'x1': 60,
                                            'line': {
                                                'color': 'white',
                                            },
                                            
                                        },
                                     {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 35,
                                            'x0': 0,
                                            'y1': 35,
                                            'x1': 10,                                         
                                            'line': {
                                                'color': 'white',
                                            },
                                            
                                        },
                                     {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 35,
                                            'x0': 10,
                                            'y1': 65,
                                            'x1': 10,
                                            'line': {
                                                'color': 'white',
                                            }
                                     },
                                    {
                                        'type': 'line',
                                        'xref': 'x',
                                        'yref': 'y',
                                        'y0': 65,
                                        'x0': 10,
                                        'y1': 65,
                                        'x1': 0,
                                        'line': {
                                            'color': 'white',
                                        }
                                      },
                                    {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 35,
                                            'x0': 100,
                                            'y1': 35,
                                            'x1': 90,                                         
                                            'line': {
                                                'color': 'white',
                                            },
                                            
                                        },
                                     {
                                            'type': 'line',
                                            'xref': 'x',
                                            'yref': 'y',
                                            'y0': 35,
                                            'x0': 90,
                                            'y1': 65,
                                            'x1': 90,
                                            'line': {
                                                'color': 'white',
                                            }
                                     },
                                    {
                                        'type': 'line',
                                        'xref': 'x',
                                        'yref': 'y',
                                        'y0': 65,
                                        'x0': 90,
                                        'y1': 65,
                                        'x1': 100,
                                        'line': {
                                            'color': 'white',
                                        }
                                      },    
                                    {
                                        'type': 'line',
                                        'xref': 'x',
                                        'yref': 'y',
                                        'y0': 100,
                                        'x0': 50,
                                        'y1': 0,
                                        'x1': 50,
                                        'line': {
                                            'color': 'white',
                                        }
                                      }, 
                                    ]
)

def draw_game(tracking_data,player_data,frame_start,frame_stop, pitch_x_length = 50, pitch_y_length = 20):
    """
    Function to draw tracking_data Dataframe, frame by frame
    
    Input:
    - tracking_data : tracking dataframe, format: frame,player1 position,player2 position, ... , playerN position
    - frame_start: first frame to draw
    - frame_stop: last frame to draw
    
    Output:
    - figure: plotly object to be showed

    """
    
    
    frames = []
    #slicing dataframe with required timeframes
    data = tracking_data[(tracking_data.index>=frame_start) & (tracking_data.index<=frame_stop)]
    for i,observation in data.iterrows():
        observation = observation.to_dict()
        ts = observation['timeframe']
        


        teams = sorted(list(set([player_data[x]['team'] for x in player_data])))

        
        frame={}
        frame['visible'] = False
        frame['mode'] = 'markers'


        frame_x=[]
        frame_y=[]
        colors = []
        text = []

        for p in data.columns[1:]: #loop on player
            
            
            frame_x.append((observation[p]['x']/pitch_x_length)*100)
            frame_y.append((observation[p]['y']/pitch_y_length)*100)
            if p not in player_data:
                color = 'grey'
            elif player_data[p]['team'] ==  teams[0]:
                color = 'red'
            else:
                color = 'blue'

            colors.append(color)
            text.append(player_data[p]['name'] if p in player_data else x)

        frame['x'] = frame_x
        frame['y'] = frame_y
        frame['marker'] = dict(color=colors, size=6) 
        frame['text'] = text
        frames.append(frame)

    return frames


def create_plot(frames):
    """
    slider creation for animation of frames. It works by setting all frames to invisible, then by setting visible the frame
    selected through the slider control
    """
    steps = []
    for i in range(0,len(frames),2):
        step = dict(
            method = 'restyle',  
            args = ['visible', [False] * (len(frames))],
        )
        for j in range(i,i+1):
            step['args'][1][j] = True # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active = 0,
        currentvalue = {"prefix": "Frame: "},
        pad = {"t": 5},
        steps = steps
    )]

    pitch_layout['sliders'] = sliders

    fig = dict(data=frames, layout=pitch_layout)

    return fig
