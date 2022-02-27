import pygame
import pandas as pd
import numpy as np
import sys


import coffee.color as c
import coffee.palletts as p

import coffee.pyg as pg
import coffee.graphers as g
import coffee.grapher as go
import coffee.graph_props as m

xls = pd.ExcelFile(
    "independent_work/Coffee Chain Visualization/PART I/data/Coffee Chain.xlsx"
)
data = pd.read_excel(xls, "Coffee Chain")

width = 1700
height = 900

active_pallett = p.milk_shake

handler = pg.handler( width, height, title="Coffee Shop Data")
main = go.Grapher(handler, (1700, 1000))

domain = m.domain(
        pos=(90, 30),
        size=( width / 2 - 100, height - 100 ))
domain2 = m.domain(
        pos=(width / 2 + 100, 30),
        size=( width / 2 - 150, height - 100 ))

area = g.area(main, data, "Marketing", "count()", "Product Type",  
    domain=domain,
    pallett=active_pallett,
    title="Quantity of Marketing Campaigns for Various Beverages Types",
).series_axis.update_visibility(False
).value_axis.update_visibility(False
).domain.update_visibility(False
).point.update_visibility(False)

distribution = g.distribution(main, data, ["Marketing"], "Product Type",  
    dir=0,
    domain=domain,
    pallett=active_pallett,
    title="",
)

area2 = g.area(main, data, "Profit", "count()", "Product Type",  
    domain=domain2,
    pallett=active_pallett,
    title="Profit for Various Beverages Types",
).series_axis.update_visibility(False
).value_axis.update_visibility(False
).domain.update_visibility(False
).point.update_visibility(False)

distribution2 = g.distribution(main, data, ["Profit"], "Product Type",  
    dir=0,
    domain=domain2, 
    pallett=active_pallett,
    title="",
)


main.graphs = [ distribution, area, distribution2, area2]
main.handler.screen.fill( active_pallett.back_RGB )
main.render()


handler.start()
