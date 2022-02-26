# Coffee-Chain-Visualization
### Exploring the data of major coffee chains

---
Although this project did not explore the dataset I found in any new and incredible way, it played a very pivotal role for how I will visualize my projects going forward. As I have worked on all the visualizations this term, either with “raw code” such as ```pygame``` (a *completely* open canvas for drawing things in python), or a pre-made one such as Altair, plotly, seaboard, or patplotlib, I noticed that almost all of my favorites were the ones that I constructed myself, with pygame. I loved the nitty gritty control over every little detail that I had, despite it being more time consuming to painstakingly align every pixel perfectly, as it gave me the exact power to do whatever I wanted.

However, while I wanted to make all my visualizations with that system, it took too long to build out the infrastructure for each project. However, however: after my previous project, Minor 6, [here](https://github.com/Brian-Masse/Animals-life-expectancy), I realized that the best course of action was not to continue building out the infrastructure for each new project, or just use a pre made visualization tool, but was in fact, **to build out my own custom one**. And so, I set off the create **B_Grapher** (name is a work in progress :) )

This is a 100% custom python model, (repo link [here](https://github.com/Brian-Masse/B_grapher) (specifically commit 3 ```Update color.py```)), that brings in my involves my custom, ultra powerful, mega color class of doom (name is *not* a work in progress :) )that I have been using so far in this term, as well as a more generalized set of classes that can handle rendering and visualizations of all kind. At the time of writing this, I have only developed the graph for distributions, as this took me **way** longer that I expected, however the concept, and more importantly, the infrastructure is there. As it is currently constructed, I am able to freely pass in the name of data columns, for both the series and and values, and have all the nitty-gritty rendering technicalities be handled for me. I have control over all colors of each element, showing and hiding some of them, and a bunch of other properties. 

As I look to expand this tool, I intend to make the axes of the graph switchable, certainly involve more visual variables, more marks, auto-layout, and a bunch of other things to make this sytem even more useable! However, for the purpose of this “demo-like” visualization  it worked perfectly!

To get a better idea of the scope and content of this specific visualization, I would highly recommend checking out the b_grapher module!

---

[Here](https://data.world/2918diy/coffee-chain) is the data set that I used

and here is the final render:

![Image](https://github.com/Brian-Masse/Coffee-Chain-Visualization/blob/main/PART%20I/exportd/final.png)
