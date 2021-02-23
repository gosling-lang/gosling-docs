Welcome to the wiki of Gosling: Grammar Of Scalable Linked Interactive Nucleotide Graphics!

Gosling is a declarative visualization grammar tailored for interactive genomic visualizations. In Gosling, users can create interactive visualizations for genomic data through a JSON syntax.

The key features of Gosling compared to existing visualization libraries are as follow:

- **Data Scalability**: As Gosling is built on [HiGlass](http://higlass.io/), the grammar allows you to handle and visualize large genome-mapped data and quickly switch the scale of visualization from base-pair resolution to the whole genome.

- **Encoding Scalability**: Gosling supports an advanced zooming technique, called *Semantic Zooming*, which allows flexible and seamless visual exploration of large genome-mapped data. This allows you to dynamically switch between different visual encoding strategies that are appropriate for given zoom scale. <!--For example, you can show nucleotide bases of genomic sequence when zoomed in while show overall distribution of the bases using stacked bar chart when zoomed out.-->

- **Expressiveness**: Gosling is designed to cover the most part of the taxonomy for genomic data visualization<sup id="fnc1">[1](#fn1)</sup>. This, for example, allows you to use a circular layout (i.e., displaying genomic coordinates in a polar system), in addition to a linear layout, and easily switch between the two.

- **Interactivity**: Gosling support diverse user interactions, including zooming and panning and brushing and linking, that are helpful for different visual analytics use cases.

---
<b id="fn1">[1]</b>: Nusrat, Harbig, and Gehlenborg, Tasks, Techniques, and Tools for Genomic Data Visualization, Computer Graphics Forum, 2019. [⏎](#fnc1)