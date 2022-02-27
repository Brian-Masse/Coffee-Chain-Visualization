import pygame
import pandas as pd
import numpy as np
import sys


import b_grapher.color as c
import b_grapher.palletts as p

import b_grapher.pyg as pg
import b_grapher.graphers as g
import coffee.grapher as go
import coffee.graph_props as m

xls = pd.ExcelFile(
    "independent_work/Coffee Chain Visualization/PART I/data/Coffee Chain.xlsx"
)
data = pd.read_excel(xls, "Coffee Chain")

width = 1700
height = 900

handler = pg.handler( width, height, title="Coffee Shop Data")
main = go.Grapher(handler, (1700, 1000))

profit = g.distribution(main, data, ["Profit"], "Product Type", 
    dir=0,
    domain=m.domain(
        pos=(150, 50),
        size=(1400, 100)), 
    title="Profit Of Various Beverage Types ($)",
    pallett=p.coffee_bean).update_series_rand( 2 )
sales = g.distribution(main, data, ["Sales"], "Product Type", 
    dir=0,
    domain=m.domain(
        pos=(150, 200),
        size=(1400, 100)), 
    title="Sales Of Various Beverage Types ($)",
    pallett=p.coffee_bean)
expenses = g.distribution(main, data, ["Total Expenses"], "Product Type", 
    dir=1,
    domain=m.domain(
        pos=(150, 400),
        size=( 1400, 100 )),
    title="Expenses Of Various Beverage Types ($)",
    pallett=p.coffee_bean
).update_series_rand( 100 )
inventory = g.distribution(main, data, ["Inventory"], "Product Type", 
    dir=1,
    domain=m.domain(
        pos=(150, 550),
        size=( 1400, 300 )),
    title="Inventory Of Various Beverage Types",
    pallett=p.coffee_bean
).update_series_rand( 20 )


main.graphs = [profit, sales, expenses, inventory]
main.handler.screen.fill( p.coffee_bean.back_RGB )
main.render()


handler.start()
