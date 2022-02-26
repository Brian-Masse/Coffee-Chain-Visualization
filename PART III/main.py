import pygame
import pandas as pd
import numpy as np
import sys


import b_grapher.color as c
import b_grapher.palletts as p

import b_grapher.pyg as pg
import b_grapher.graphers as g
import b_grapher.grapher as go
import b_grapher.graph_props as m

xls = pd.ExcelFile(
    "independent_work/Coffee Chain Visualization/PART I/data/Coffee Chain.xlsx"
)
data = pd.read_excel(xls, "Coffee Chain")

width = 1700
height = 900

active_pallett = p.blue_lagoon

handler = pg.handler( width, height, title="Coffee Shop Data")
main = go.Grapher(handler, (1700, 1000))

sales = g.distribution(main, data, ["Sales"], "Product", 
    dir=1,
    domain=m.domain(
        pos=(150, 50),
        size=(1400, 170)), 
    title="Sales Of Various Beverages",
    pallett=active_pallett).update_series_rand( 2 )
sales2 = g.distribution(main, data, ["Sales"], "Product Type", 
    dir=1,
    domain=m.domain(
        pos=(150, 270),
        size=(1400, 170)),
    point=m.point(
        radius=4,
        stroke=3),
    title="Sales Of Various Beverage Types",
    pallett=active_pallett)

marketing = g.distribution(main, data, ["Marketing"], "Product Type", 
    dir=0,
    domain=m.domain(
        pos=(150, 550),
        size=( 600, 300 )),
    point=m.point(
        radius=10,
        stroke=2,
        shape=4),
    pallett=active_pallett,
    title="tity of Marketing Campaigns for Various Beverages Types",).update_series_rand(1)
marketing2 = g.distribution(main, data, ["Marketing"], "Product", 
    dir=0,
    domain=m.domain(
        pos=(900, 550),
        size=( 550, 300 )),
    point=m.point(
        radius=4,
        shape=3),
    pallett=active_pallett,
    title="Quantity of Marketing Campaigns for Various Beverages",
)


main.graphs = [sales, sales2, marketing, marketing2]
main.handler.screen.fill( active_pallett.back_RGB )
main.render()


handler.start()
