### Welcome to the wiki of Gosling!

Gosling (Grammar Of Scalable Linked Interactive Nucleotide Graphics) is a declarative visualization grammar tailored for interactive genomic visualizations. In Gosling, users can create interactive visualizations for genomic data through a JSON syntax.

### Key Features
The key features of Gosling compared to existing visualization libraries and grammars are as follows:

- **Data Scalability**: As Gosling is built on [HiGlass](http://higlass.io/), the grammar allows you to handle and visualize large genome-mapped data and quickly switch the scale of visualization from base-pair resolution to whole genome.

- **Encoding Scalability**: Gosling supports an advanced zooming technique, called [*Semantic Zooming*](https://infovis-wiki.net/wiki/Semantic_Zoom), which allows flexible and seamless visual exploration of large genome-mapped data. This allows you to dynamically switch between different visual encoding strategies that are appropriate for given zoom scale. <!--For example, you can show nucleotide bases of genomic sequence when zoomed in while show overall distribution of the bases using stacked bar chart when zoomed out.-->

- **Expressiveness**: Gosling is designed to cover the most part of the [taxonomy for genomic data visualization](https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.13727). For example, this allows you to use a circular layout (i.e., displaying genomic coordinates in a polar system), in addition to a linear layout, and easily switch between the two.

- **Interactivity**: Gosling supports intuitive and effective user interactions, including zooming and panning and [brushing and linking](https://infovis-wiki.net/wiki/Linking_and_Brushing), that help you flexibly set up visualization reflecting your different visual analytics use cases.
