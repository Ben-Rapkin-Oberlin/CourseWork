from django.shortcuts import render
from charts.models import Chart
import pandas as pd
from plotly.offline import plot
import plotly.express as px



def index(request):
    qs = Chart.objects.all()
    #qs is a queryset, meaning that it is 
    #a data structure that contains a list of objects
    #from the database

    #Below is creating a list of dictionaries
    #from the queryset

    #I believe that this specifically creates
    #a list of two dictionaries, one for each graph we created

    projects_data = [
        {
            'Project': x.name,
            'Start': x.start_date,
            'Finish': x.finish_date,
            'Responsible': x.responsible.username
        } for x in qs
    ]

    #print(projects_data)

    df = pd.DataFrame(projects_data)
    #print(df.head())
    #(-> input output)
    #This is where we start creating the graphs
    fig = px.timeline(
        df, x_start="Start", x_end="Finish", y="Project", color="Responsible"
    )
    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")
    context = {'plot_div': gantt_plot}
    return render(request, 'index.html', context)


def table(request):
    data = pd.read_csv('monks1.csv')
    data_html = data.to_html()
    context = {'loaded_data': data_html}
    return render(request, "dataflow/table.html", context)