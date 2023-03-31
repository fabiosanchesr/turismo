import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
#from app import *
#from dash import html, callback, Input, Output, State, ctx


dash.register_page(__name__)

# # Login screen
# layout = html.Form(
#     [
#         html.H2("Please log in to continue:", id="h1"),
#         dcc.Input(placeholder="Enter your username", type="text", id="uname-box", name='username'),
#         dcc.Input(placeholder="Enter your password", type="password", id="pwd-box", name='password'),
#         html.Button(children="Login", n_clicks=0, type="submit", id="login-button"),
#         html.Div(children="", id="output-state")
#     ], method='POST'
# )


layout = dbc.Container([
    dbc.Col([
        dbc.Row([
            dbc.Tabs(
                [dbc.Tab(
                    [
                        dbc.Card(
                            dbc.CardBody([
                                html.Form([
                                    dbc.Col([
                                        dbc.Row([
                                            dbc.Label('Username', html_for='login-user'),
                                            dcc.Input(placeholder='Enter your username', type='text', id='login-user', name='username', className='form-control'),
                                        ]),
                                        dbc.Row([
                                            dbc.Label('Password', html_for='login-pass'),
                                            dcc.Input(placeholder='Enter your password', type='password', id='login-pass', name='password', className='form-control')
                                        ],class_name='mt-3'),
                                        dbc.Row(html.Button(children="Log In", n_clicks=0, type="submit", id="login-button", className='btn mt-3 m-auto', style={'width':'25%'}))
                                    ], class_name='ms-3 me-3 mt-1')
                                ], method='POST')
                            ])
                        )
                    ], label='Log In', tab_id='login', tab_style={'width':'50%'}, label_style={'width':'100%'}
                ),
                dbc.Tab(
                    [dbc.Card(
                        dbc.CardBody([
                            html.Form([
                                dbc.Col([
                                    dbc.Row([
                                        dbc.Label('Username/E-mail', html_for='register-user'),
                                        dbc.Input(type='text', id='register-user', class_name='form-control'),
                                    ],class_name='mt-3'),
                                    dbc.Row([
                                        dbc.Label('Password', html_for='register-pass'),
                                        dbc.Input(type='password', id='register-pass', class_name='form form-control')
                                    ],class_name='mt-3'),
                                    dbc.Row([
                                        dbc.Label('E-mail', html_for='register-email'),
                                        dbc.Input(type='email', id='register-email', class_name='form form-control ')
                                    ],class_name='mt-3'),
                                    dbc.Row(dbc.Button('Register', id='btn-register',class_name='mt-3 m-auto', style={'width':'25%'}))

                                ], class_name='ms-3 me-3 mt-1')
                            ])
                        ],class_name='mt-3')
                        )],label='Register', tab_id='register', tab_style={'width':'50%'}, label_style={'width':'100%'}
                    ),
                ],
                active_tab='login')
            ],
            className='g-0'
        )], class_name='my-auto'),
        dbc.Row("", id='output-state', class_name='g-0 mt-5')
    ], id='main-login'
)