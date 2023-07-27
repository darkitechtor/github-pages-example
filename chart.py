import plotly.graph_objects as go
import plotly.offline as pyo

def save_chart_to_html():
    x_data = [1, 2, 3, 4, 5]
    y_data = [10, 25, 8, 30, 15]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_data,
                            y=y_data,
                            mode='lines',
                            name='Line Chart')
    )
    fig.update_layout(title='Simple Line Chart',
                        xaxis_title='X-axis',
                        yaxis_title='Y-axis'
    )

    pyo.plot(fig, filename='line_chart.html')

save_chart_to_html()