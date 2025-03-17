import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

# Создаем Dash-приложение
app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1("Заявки"),
    dcc.Dropdown(id='workorder-dropdown', placeholder="Выберите заявку"),
    html.Div(id='approval-data')
])

# Callback для загрузки списка заявок
@app.callback(
    Output('workorder-dropdown', 'options'),
    [Input('workorder-dropdown', 'id')]
)
def fetch_workorders(_):
    response = requests.get('http://localhost:8000/workorder/')
    if response.status_code == 200:
        workorders = response.json()
        return [{'value': workorder['workorderid'], 'label': workorder['description']} for workorder in workorders]
    return []

# Callback для отображения данных о согласовании заявки
@app.callback(
    Output('approval-data', 'children'),
    [Input('workorder-dropdown', 'value')]
)
def display_approval(workorderid):
    if not workorderid:
        return None
    response = requests.get(f'http://localhost:8000/approval/?workorderid={workorderid}')
    if response.status_code == 200:
        approval_list = response.json()
        print(approval_list)
        if not approval_list:
            return "В системе нет данных о согласовании."
        
        response = requests.get(f'http://localhost:8000/user/')
        if response.status_code == 200:
            user_list = response.json()
            if not user_list:
                return "В системе нет данных о пользователях."
            user_dict = {user['userid']: user['displayname'] for user in user_list}
        return html.Ul([
            html.Li(f"Согласующий: {user_dict[approval['userid']]}, cтатус согласования: {approval['status']}") if workorderid == approval['workorderid'] else None for approval in approval_list
        ])
    return "Ошибка загрузки данных."

if __name__ == '__main__':
    app.run_server(debug=True)