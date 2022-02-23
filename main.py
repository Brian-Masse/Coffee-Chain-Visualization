import pygame
import pandas as pd
import numpy as np
import sys

import b_grapher.pyg as pg
import b_grapher.color as c

import b_grapher.graphers as g
import b_grapher.grapher as go

xls = pd.ExcelFile(
    "independent_work/Coffee Chain Visualization/data/Coffee Chain.xlsx"
)
data = pd.read_excel(xls, "Coffee Chain")

width = 1700
height = 600

handler = pg.handler( width, height )
main = go.Grapher(handler, (1700, 1000))

profit = g.distribution(main, data, ["Profit"], "Product Type", 
    size=(1450, 100), 
    pos=(200, 100),
    title="Profit Of Various Beverage Types ($)")
sales = g.distribution(main, data, ["Sales"], "Product Type", 
    size=(1450, 100), 
    pos=(200, 250),
    title="Sales Of Various Beverage Types ($)")
expenses = g.distribution(main, data, ["Total Expenses"], "Product Type", 
    size=(1450, 100), 
    pos=(200,400),
    title="Expenses Of Various Beverage Types ($)")

main.graphs = [profit, sales, expenses]
main.handler.screen.fill( ( 140, 171, 160 ) )
main.render()





handler.start()
