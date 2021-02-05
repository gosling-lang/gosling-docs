## Create your visualizations using Gosling ＼（＾▽＾）／

This tutorial will guide you step by step in writing the JSON specification to create an interactive visualization in Gosling. You are encouraged to follow the tutorial and create visualizations in the [online editor](onlineEditorURL).

## Loading Data

In this tutorial, we use a CSV data ([the complete data file](csvDataURL)).



|Chromosome|chromStart|chromEnd|Name|Stain|
|---|---|---|---|--|
|chr1|0|2300000|p36.33|gneg|
|chr1|2300000|5300000|p36.32|gpos25|
|chr1|5300000|7100000|p36.31|gneg|
|...|


To start with, we load this data through URL to a visualization (i.e., a `track`).
The `track.data` property specifies how to fetch and process the data.
```javascript

{
    "tracks":[{
        // Load a csv data file through URL
        "data": {
            "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
            "type": "csv",
            "genomicFields": ["chromStart", "chromEnd"]
        }
    }]
}
```

## Encoding Data with Marks
After loading the data, we now specify how to visualize the data.
This process is achieved by binding the values of data fields to the visual channels (e.g., color, size) of a graphic element (i.e., `mark`).

Let's say we use a `rect` mark for the loaded csv data.
Each `rect` represents a chromosome. 
The x-coordinate of the mark's start (`x`) and end (`xe`) position indicate the chromStart and the chromeEnd, respectively.
The `color` indicates the stain value. 

For each visual channel, Gosling creates a mapping from the values of the data field (e.g., [gnes, gpos25, gpos50, ...]) to the values of the visual channel (e.g., color). We call the values of data field **domain** and the values of the visual channel **range**.
This mapping is specified by the following properties:
| visual channel properties | type                        | description                                                                        |
| ------------------------- | --------------------------- | ---------------------------------------------------------------------------------- |
| field                     | string                      | specify name of the data field                                                     |
| type                      | string                      | specify type of the data field. support `"genomic"`, `"nominal"`, `"quantitative"` |
| domain                    | [number, number]\| string[] | specify values of the data field                                                   |
| range                     | [number, number]\| string[] | specify values of the visual channel                                               |


```javascript
{
    "tracks":[{
        // Load a csv data file through URL
        "data": {
            "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
            "type": "csv",
            "genomicFields": ["chromStart", "chromEnd"]
        },
        // specify the mark type
        "mark": "rect",
        // encoding data with visual channels
        "x": {
            "field": "chromStart",
            "type": "genomic",
            "domain": {"chromosome": "1"},
            "axis": "top"
        },
        "xe": {"field": "chromEnd", "type": "genomic"},
        "color": {
            "field": "Stain", 
            "type": "nominal",
            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
            "range": ["white","#D9D9D9","#979797","#636363", "black","#A0A0F2"]
        }
    }]
}
```

**:tada::tada::tada::tada::tada::tada::tada::tada:**  
**You have just created a scalable and interactive visualization in Gosling!**  
You can interact with the visualization you just created in the online editor through zoom and pan.
Or, you can keep reading the tutorial and make your visualizations even more fancy.

## Data Transform
Gossling supports filtering out uninterested data through the `dataTransform` property.
For example, we can add a filter to only visualize chromosomes whose stain result is one of "gpos25", "gpos50", "gpos75", or "gpos100".

```diff
{
    "tracks":[{
        "data": {
            "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
            "type": "csv",
            "genomicFields": ["chromStart", "chromEnd"]
        },       
+        "dataTransform": {
+            "filter": [{"field": "Stain", oneOf: ["gpos25", "gpos50", "gpos75", "gpos100"]}]
+        },
        "mark": "rect",
        "x": {
            "field": "chromStart",
            "type": "genomic",
            "domain": {"chromosome": "1"},
            "axis": "top"
        },
        "xe": {"field": "chromEnd", "type": "genomic"},
        "color": {
            "field": "Stain", 
            "type": "nominal",
            "domain": ["gpos25", "gpos50", "gpos75", "gpos100"],
            "range": ["#D9D9D9","#979797","#636363", "black"]
        }
    }]
}
```



## Superposing Multiple Marks
Multiple `mark` shapes can be put on the top of one another through the `superpose` property.
In the code below, a chromosome is visualized as a `triangle-r` mark if its stain result is `acen` and its name includes `q`; a chromosome is visualized as a `triangle-l` mark if its stain result is `acen` and its name includes `p`. The `rect` mark, the `triangle-r` mark, and the `triangle-l` mark are superposed on the same genomic coordinate through the `superpose` property.

```diff
{
    "tracks":[{
        "data": {
            "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
            "type": "csv",
            "genomicFields": ["chromStart", "chromEnd"]
        },       
        "dataTransform": {
            "filter": [{"field": "Stain", oneOf: ["gpos25", "gpos50", "gpos75", "gpos100"]}]
        },
        "mark": "rect",
        "x": {
            "field": "chromStart",
            "type": "genomic",
            "domain": {"chromosome": "1"},
            "axis": "top"
        },
        "xe": {"field": "chromEnd", "type": "genomic"},
        "color": {
            "field": "Stain", 
            "type": "nominal",
            "domain": ["gpos25", "gpos50", "gpos75", "gpos100"],
            "range": ["#D9D9D9","#979797","#636363", "black"]
        },
+       "superpose":[
+           {
+             "mark": "triangle-r",
+             "dataTransform": {
+               "filter": [
+                 {"field": "Stain", "oneOf": ["acen"]},
+                 {"field": "Name", "include": "q"}
+               ]
+             },
+             "color": {"value": "#B40101"}
+           },
+           {
+             "mark": "triangle-l",
+             "dataTransform": {
+               "filter": [
+                 {"field": "Stain", "oneOf": ["acen"]},
+                 {"field": "Name", "include": "p"}
+               ]
+             },
+             "color": {"value": "#B40101"}
+           }
+       ]
    }]
}
```

## Customize Style

You can freely modify the size of the visualization, add a title, or change the layout.
Gosling supports easy creation of circular layout through the `layout` property.

```diff
{
+   "title": "Get Started Example",
+   "layout": "circular",
    "tracks":[{
        "data": {
            "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
            "type": "csv",
            "genomicFields": ["chromStart", "chromEnd"]
        },       
        "dataTransform": {
            "filter": [{"field": "Stain", oneOf: ["gpos25", "gpos50", "gpos75", "gpos100"]}]
        },
        "mark": "rect",
        "x": {
            "field": "chromStart",
            "type": "genomic",
            "domain": {"chromosome": "1"},
            "axis": "top"
        },
        "xe": {"field": "chromEnd", "type": "genomic"},
        "color": {
            "field": "Stain", 
            "type": "nominal",
            "domain": ["gpos25", "gpos50", "gpos75", "gpos100"],
            "range": ["#D9D9D9","#979797","#636363", "black"]
        },
        "superpose":[
            {
              "mark": "triangle-r",
              "dataTransform": {
                "filter": [
                  {"field": "Stain", "oneOf": ["acen"]},
                  {"field": "Name", "include": "q"}
                ]
              },
              "color": {"value": "#B40101"}
            },
            {
              "mark": "triangle-l",
              "dataTransform": {
                "filter": [
                  {"field": "Stain", "oneOf": ["acen"]},
                  {"field": "Name", "include": "p"}
                ]
              },
              "color": {"value": "#B40101"}
            }
        ],
+       "width": 1000,
+       "height": 200
    }]
}
```


## More Examples
You can find more examples [here](exampleURL).

[onlineEditorURL]: http://gosling.js.org
[exampleURL]: http://gosling.js.org
[csvDataURL]: https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv
