from dash import html, dcc
import dash_bootstrap_components as dbc


class Layout:
    def __init__(self, symbol_dict: dict) -> None:
        self._symbol_dict = symbol_dict

        self._stock_options_dropdown = [
            {"label": name, "value": symbol} for symbol, name in symbol_dict.items()
        ]

        self._ohlc_options = [
            {"label": option, "value": option}
            for option in ("open", "high", "low", "close")
        ]

        self._slider_marks = {
            i: mark
            for i, mark in enumerate(
                ["1 day", "1 week", "1 month", "3 months", "1 year", "5 year", "Max"]
            )
        }

    def layout(self):
        return dbc.Container(
            [
                dbc.Card(
                    dbc.CardBody(html.H1("Techy stocks viewer")), className="mt-3"
                ),
                dbc.Row(
                    className="mt-4",
                    children=[
                        dbc.Col(html.P("Choose a stock"), className="mt-1"),

                        dbc.Col(
                            dcc.Dropdown(
                                id="stockpicker-dropdown",
                                options=self._stock_options_dropdown,
                                value="AAPL",
                            ), lg = "4",
                        ),

                        dbc.Col(
                            dbc.Card(
                                dcc.RadioItems(
                                    id="ohlc-radio",
                                    className="m-1",
                                    options=self._ohlc_options,
                                    value="close",
                                )
                            )
                        ),
                    ],
                ),
                html.P(id="highest-value"),
                html.P(id="lowest-value"),
                dcc.Graph(id="stock-graph"),
                dcc.Slider(
                    id="time-slider",
                    min=0,
                    max=6,
                    marks=self._slider_marks,
                    value=2,
                    step=None,
                ),
                # storing intermediate value on clients browser in order to share between several callbacks
                dcc.Store(id="filtered-df"),
            ]
        )