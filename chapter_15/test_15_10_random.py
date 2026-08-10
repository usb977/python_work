import plotly.graph_objects as go
import numpy as np

l = 1000
x_steps = np.random.choice([-1, 1], size=l) + 0.2 * np.random.randn(l)
y_steps = np.random.choice([-1, 1], size=l) + 0.2 * np.random.randn(l)

# 起点设为 (0, 0)
x_position = np.concatenate(([0], np.cumsum(x_steps)))
y_position = np.concatenate(([0], np.cumsum(y_steps)))

fig = go.Figure()

# 主路径
fig.add_trace(go.Scatter(
    x=x_position,
    y=y_position,
    mode='markers',
    name='Random Walk',
    marker=dict(
        color=np.arange(len(x_position)),
        size=6,
        colorscale='Greens',
        showscale=True
    )
))

# 起点（绿色）
fig.add_trace(go.Scatter(
    x=[x_position[0]],
    y=[y_position[0]],
    mode='markers',
    name='Start (0, 0)',
    marker=dict(color='green', size=12, symbol='star')
))

# 终点（红色）
fig.add_trace(go.Scatter(
    x=[x_position[-1]],
    y=[y_position[-1]],
    mode='markers',
    name='End',
    marker=dict(color='red', size=12, symbol='star')
))

fig.show()