# PART II

--- 

![Image](https://github.com/Brian-Masse/Coffee-Chain-Visualization/blob/main/PART%20II/exports/final.png)

In this visualization, described by "Distribution: Strips", I thought it would be a good idea to look into how I can rotate the axes and their data. Specifically, how I could get the values vertically, and the series horizontally (creating different “strips” so it fits the prompt of this project perfectly! ) I felt that this was a good next step, as I assumed that this would likely involve restructuring some of my code to make it more object oriented, and thus give it a stronger, more versatile foundation to rest on. *(turns out, I was right!)* 

This update to the grapher gives a much more solid foundation for the entire system, as it enables use of common features across graphs (```domain```, ```axis```) without tying them to any specific visualization (ie. A distribution vis), and an easy way to customize them, without needing to tunnel into the actual structure of the objects. Accomplishing this rotation was both a combination of making certain elements of a vis into specific objects, and some fancy math for positioning everything. The customization is silly a growing list of functions that alters a part of the graph (or one of its properties), and then returns the graph, so a user can chain customizing functions together. While the resulting graph does not look all top dissimilar from the first one in part I, the infrastructure that enables it is far superior!

In this visualization, as I did last time, I chose the series from the data mostly at random. Here however, I modeled 4 series, so I could showcase the different orientation / layout possibilities that my system now offers!I am super excited to continue to work on this module to create an even more well-rounded, applicable system!

---

## Here are all my links:
1. [data](https://data.world/2918diy/coffee-chain)
2. [grapher](https://github.com/Brian-Masse/B_grapher) commit 4, ```rotating the axes```
3. [Part I]( https://github.com/Brian-Masse/Coffee-Chain-Visualization/tree/main/PART%20I )
4. [Inspiration Project](https://github.com/Brian-Masse/Animals-life-expectancy)

