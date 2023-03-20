import functools
import json
from turtle import home
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, send_file
)
import matplotlib
matplotlib.use('agg') # This needs to happen before any pyplot import!!!
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns
import pandas as pd
import os.path
import numpy as np
import holoviews as hv
from bokeh.embed import components
import holoviews as hv

home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/http_floods', methods=('GET', 'POST'))
def httpflood():
    #call function to generate hvplot here to get script and div
    script1, div1 = components(hvplot_1())
    script2, div2 = components(hvplot_2())
    script3, div3 = components(hvplot_3())

    #pass the script and div to render template to get the graph on html
    return render_template('http_flood.html', hv_script1=script1, hv_div1=div1, hv_script2=script2, hv_div2=div2, hv_script3=script3, hv_div3=div3)
    
@home_bp.route('/syn_floods', methods=('GET', 'POST'))
def synflood():

    script4, div4 = components(hvplot_4())
    script5, div5 = components(hvplot_5())
    script6, div6 = components(hvplot_6())

    return render_template('syn_flood.html',hv_script4=script4, hv_div4=div4, hv_script5=script5, hv_div5=div5, hv_script6=script6, hv_div6=div6)

@home_bp.route('/udp_floods', methods=('GET', 'POST'))
def udpflood():
    
    script7, div7 = components(hvplot_7())
    script8, div8 = components(hvplot_8())
    script9, div9 = components(hvplot_9())
    
    return render_template('udp_flood.html', hv_script7=script7, hv_div7=div7, hv_script8=script8, hv_div8=div8, hv_script9=script9, hv_div9=div9)

@home_bp.route('/dashboard', methods=('GET', 'POST'))
def pywedge():
    return render_template('dashboard.html')

# (2)
def _mpl_to_png_bytestring(fig):
    """This function uses Matplotlib's FigureCanvasAgg backend to convert a MPL
    figure into a PNG bytestring. The bytestring is not encoded in this step."""
    
    import io
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg

    if isinstance(fig, plt.Axes):
        fig = fig.figure
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)

    return output.getvalue()


def mpl_to_html(fig, **kwargs):
    """Take a figure and render it directly to HTML. A PNG is created, and
    then encoded into base64 and decoded back to UTF-8 so that it can be stored
    inside a <img> HTML tag."""
    
    from flask import Markup
    import base64

    bstring = _mpl_to_png_bytestring(fig)
    png = base64.b64encode(bstring).decode('utf8')
    options = ' '.join([f'{key}="{val}"' for key, val in kwargs.items()])

    return Markup(f'<img src="data:image/png;base64,{png}" {options}>')


def render_mpl(fig):
    """This function returns a png file from a Matplotlib figure or subplots
    object. It is designed to be at the bottom of an endpoint function; instead
    of returning HTML or ``render_template()``, you return this instead.
    """
    from flask import Response
    return Response(_mpl_to_png_bytestring(fig), mimetype='image/png')


#get dataset HTTP Flows
def getHTTPFlows():
    rootdir = os.path.abspath(os.path.dirname(__file__))
    #read dataset into pandas
    dataset = pd.read_csv(os.path.join(rootdir, 'static/dataset_files/HTTP_Flows.csv'))
    return dataset

#get dataset SYN Flows
def getSYNFlows():
    rootdir = os.path.abspath(os.path.dirname(__file__))
    #read dataset into pandas
    dataset = pd.read_csv(os.path.join(rootdir, 'static/dataset_files/SYN_Flows.csv'))
    return dataset

#get dataset HTTP Flows
def getUDPFlows():
    rootdir = os.path.abspath(os.path.dirname(__file__))
    #read dataset into pandas
    dataset = pd.read_csv(os.path.join(rootdir, 'static/dataset_files/UDP_Flows.csv'))
    return dataset

def hvplot_1():
    #Generate sample hvplot
    df = getHTTPFlows()
    import hvplot.pandas
    pd.options.plotting.backend = 'holoviews'

    graph = df.hvplot.line(x='pr', y=['attack_a', 'attack_t'])
    return hv.render(graph)

def hvplot_2():
    #Generate sample hvplot
    df = getHTTPFlows()
    import hvplot.pandas
    pd.options.plotting.backend = 'holoviews'

    graph = df.hvplot.bar(x='pr', y='attack_a')
    return hv.render(graph)

def hvplot_3():
    #Generate sample hvplot
    df = getHTTPFlows()
    import hvplot.pandas
    pd.options.plotting.backend = 'holoviews'

    graph = df.hvplot.box(y='dp')
    return hv.render(graph)

def hvplot_4():
    #Generate sample hvplot
    df = getSYNFlows()
    import hvplot.pandas
    pd.options.plotting.backend = 'holoviews'

    graph = df.hvplot.line(x='pr', y=['attack_a', 'attack_t'])
    return hv.render(graph)

def hvplot_5():
    #Generate sample hvplot
    df = getSYNFlows()
    import hvplot.pandas
    pd.options.plotting.backend = 'holoviews'

    graph = df.hvplot.bar(x='pr', y='attack_a')
    return hv.render(graph)

def hvplot_6():
    #Generate sample hvplot
    df = getSYNFlows()
    import hvplot.pandas
    pd.options.plotting.backend = 'holoviews'

    graph = df.hvplot.box(y='dp')
    return hv.render(graph)

def hvplot_7():
    #Generate sample hvplot
    df = getUDPFlows()
    import hvplot.pandas
    pd.options.plotting.backend = 'holoviews'

    graph = df.hvplot(x='pr', y=['attack_a', 'attack_t'])
    return hv.render(graph)

def hvplot_8():
    #Generate sample hvplot
    df = getUDPFlows()
    import hvplot.pandas
    pd.options.plotting.backend = 'holoviews'

    graph = df.hvplot.bar(x='pr', y='attack_a')
    return hv.render(graph)

def hvplot_9():
    #Generate sample hvplot
    df = getUDPFlows()
    import hvplot.pandas
    pd.options.plotting.backend = 'holoviews'

    graph = df.hvplot.box(y='dp')
    return hv.render(graph)
