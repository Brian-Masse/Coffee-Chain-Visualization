# PART III

![Image](https://github.com/Brian-Masse/Coffee-Chain-Visualization/blob/main/PART%20III/exports/Final.png)


For this visualization, ```Distributions: Circular``` I thought it would be good to look at the customizability and universality of mark types. In the end, I would love to have a variety of mark types, that can all be customized through one place, easily, while also useable in a variety of visualizations and contexts. While this was considerably easier task than last project’s rotational series, it posed a unique set of challenges and required me to further modularize my module code! In the abstract, I created a new class (that one day will hopefully be part of a larger number of similar classes) that contains all the data and functions for the ```marl point```. Instead of delegating all rendering processes to the handler, the mark now gets a copy of the handler, and uses that to render itself. This means that I can involve more advanced aspects of rendering (such as transparency, strokes, and shape) without cluttering the handler. This class then gets passed into the distribution class, and in that visualization's render function, the render function of this mark gets called. Although not the most involved solution, I think that its simplicity will enable this (and future marks) to be used in a wider range of contexts. 

Soon I hope to add more customizability to other aspects of the graph, such as series titles, series ticks, vis title, and domain, but this was a good proof of concept to see how I might successfully add those features. I would also like to, in the future, be able to handle and render multiple series on one visualization, as this will create a level of nuance and conciseness  that my visualizations currently can't achieve. 

I am still super excited about this project, and the progress that I have made on it, and cannot wait to continue advancing it in the future! 

*(also I changed the name from b_grapher, to **cofee** which I think is not only 1000 million times better, but the most important change that I have made so far!)


## Here are all my links:
1. [data](https://data.world/2918diy/coffee-chain)
2. [coffee](https://github.com/Brian-Masse/B_grapher) commit 6, ```changing the name```
3. [Part I]( https://github.com/Brian-Masse/Coffee-Chain-Visualization/tree/main/PART%20I )
4. [Part II]( https://github.com/Brian-Masse/Coffee-Chain-Visualization/tree/main/PART%20II )
5. [Inspiration Project](https://github.com/Brian-Masse/Animals-life-expectancy)

