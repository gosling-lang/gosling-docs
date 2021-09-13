---
title: Multi-track Visualizations
---
In [Tutorial 1](https://github.com/gosling-lang/gosling-docs/blob/master/tutorials/create-single-track-visualization.md), we introduce how to load data, encode data with marks, transform data, overlay multiple marks and obtain the following visualization.
<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/tutorial/tutorial_overlay.png" alt="gosling vis overlay" width="800"/>
<details>
  <summary>click to expand the code</summary>

```javascript
{
    "tracks":[{
        "width": 700,
        "height": 70,
        "data": {
            "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
            "type": "csv",
            "chromosomeField": "Chromosome",
            "genomicFields": ["chromStart", "chromEnd"]
        },   
        "x": {
            "field": "chromStart",
            "type": "genomic",
            "domain": {"chromosome": "1"},
            "axis": "top"
        },
        "xe": {"field": "chromEnd", "type": "genomic"},
        "alignment": "overlay",
        "tracks":[
             {
             "mark": "rect",
             "dataTransform": [{"type":"filter", "field": "Stain", "oneOf": ["acen"], "not": true}],
             "color": {
                 "field": "Stain", 
                 "type": "nominal",
                 "domain": ["gpos25", "gpos50", "gpos75", "gpos100"],
                 "range": ["#D9D9D9","#979797","#636363", "black"]
             }
             },
            {
              "mark": "triangleRight",
              "dataTransform": [
                  {"type":"filter", "field": "Stain", "oneOf": ["acen"]},
                  {"type":"filter", "field": "Name", "include": "q"}
                ],
              "color": {"value": "#B70101"}
            },
            {
              "mark": "triangleLeft",
              "dataTransform": [
                  {"type":"filter", "field": "Stain", "oneOf": ["acen"]},
                  {"type":"filter", "field": "Name", "include": "p"}
                ],
              "color": {"value": "#B70101"}
            }
        ],
        "size": {"value": 20},
        "stroke": {"value": "gray"},
        "strokeWidth": {"value": 0.5}
    }]
}
```
</details>

This tutorial continues from this example and introduces more advances functions: 
- [Semantic Zooming](#semantic-zooming)
- [Multiple Linked Tracks](#multiple-linked-tracks)
- [Circular Layout](#circular-layout)


## Semantic Zooming

Apart from the default zoom and pan interactions, [semantic zoom](https://github.com/gosling-lang/gosling-docs/blob/master/docs/semantic-zoom.md) is supported in Gosling and allows users to switch between different visualizations of the same data through zooming in/out. When zooming in, the same data will be represented in a different way in which more details are shown. 

Let's say, for this visualization, we want text annotations to show up when zooming in.
We add `text` marks to the `overlay` property and specify when the `text` marks should appear through the `visibility` property.
We may wish the text marks to appear when the distance between chromStart and chromEnd is big enough to place a text mark.
In other words, the text marks appear when the width (`measure`) of the text mark (`target`) is less than (`operation`) than `|xe-x|`.


<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/tutorial/tutorial_text_label.png" alt="gosling semantic zoom" width="800"/>

```diff
{
  "tracks": [
    {
      "width": 700,
      "height": 70,
      "data": {
        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
        "type": "csv",
        "chromosomeField": "Chromosome",
        "genomicFields": ["chromStart", "chromEnd"]
      },
      "x": {
        "field": "chromStart",
        "type": "genomic",
        "domain": {"chromosome": "1"},
        "axis": "top"
      },
      "xe": {"field": "chromEnd", "type": "genomic"},
      "alignment": "overlay",
      "tracks": [
+        {
+          "mark": "text",
+          "dataTransform": [{"type":"filter", "field": "Stain", "oneOf": ["acen"], "not": true}],
+          "text": {"field": "Name", "type": "nominal"},
+          "color": {
+            "field": "Stain",
+            "type": "nominal",
+            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
+            "range": ["black", "black", "black", "black", "white", "black"]
+          },
+          "visibility": [
+            {
+              "operation": "less-than",
+              "measure": "width",
+              "threshold": "|xe-x|",
+              "target": "mark"
+            }
+          ],
+          "style": {"textStrokeWidth": 0}
+        },
        {
          "mark": "rect",
          "dataTransform": [{"type":"filter", "field": "Stain", "oneOf": ["acen"], "not": true}],
          "color": {
            "field": "Stain",
            "type": "nominal",
            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
            "range": [
              "white",
              "#D9D9D9",
              "#979797",
              "#636363",
              "black",
              "#A0A0F2"
            ]
          }
        },
        {
          "mark": "triangleRight",
          "dataTransform": [
              {"type":"filter", "field": "Stain", "oneOf": ["acen"]},
              {"type":"filter", "field": "Name", "include": "q"}
            ],
          "color": {"value": "#B40101"}
        },
        {
          "mark": "triangleLeft",
          "dataTransform": [
              {"type":"filter", "field": "Stain", "oneOf": ["acen"]},
              {"type":"filter", "field": "Name", "include": "p"}
            ],
          "color": {"value": "#B40101"}
        }
      ],
      "size": {"value": 20},
      "stroke": {"value": "gray"},
      "strokeWidth": {"value": 0.5}
    }
  ]
}
```


## Multiple Linked Tracks

We may wish to represent the same data from different aspects using different types of visualization.
To achieve this, we add an area chart (i.e., a new `track`) to the `tracks` property. 
Since these tracks share the same `x` coordinate, we wish to link these two tracks: the zooming and panning performed in one track will be automatically applied to the linked track.  
In Gosling, `tracks` can be linked by assigning `x` the same  `linkingId`. 


<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/tutorial/tutorial_multi_track.png" alt="gosling multi tracks" width="800"/>

```diff
{
+ "spacing": 5,  
  "tracks": [
+     {
+      "width": 700,
+      "height": 40,  
+      "data": {
+        "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
+        "type": "multivec",
+        "row": "sample",
+        "column": "position",
+        "value": "peak",
+        "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
+      },
+      "mark": "area",
+      "x": {
+        "field": "position",
+        "type": "genomic",
+        "domain": {"chromosome": "1"},
+        "axis": "top",
+        "linkingId": "link-1"
+      },
+      "y": {"field": "peak", "type": "quantitative"},
+      "color": {"field": "sample", "type": "nominal"}
+    },
    {
      "width": 700,
-     "height": 70,
+     "height": 20,
      "data": {
        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
        "type": "csv",
        "chromosomeField": "Chromosome",
        "genomicFields": ["chromStart", "chromEnd"]
      },
      "x": {
        "field": "chromStart",
        "type": "genomic",
        "domain": {"chromosome": "1"},
-        "axis": "top"
+        "linkingId": "link-1"
      },
      "xe": {"field": "chromEnd", "type": "genomic"},
      "alignment": "overlay",
      "tracks": [
        {
          "mark": "text",
          "dataTransform": [{"type":"filter", "field": "Stain", "oneOf": ["acen"], "not": true}],
          "text": {"field": "Name", "type": "nominal"},
          "color": {
            "field": "Stain",
            "type": "nominal",
            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
            "range": ["black", "black", "black", "black", "white", "black"]
          },
          "visibility": [
            {
              "operation": "less-than",
              "measure": "width",
              "threshold": "|xe-x|",
              "transitionPadding": 10,
              "target": "mark"
            }
          ],
          "style": {"textStrokeWidth": 0}
        },
        {
          "mark": "rect",
          "dataTransform": [{"type":"filter", "field": "Stain", "oneOf": ["acen"], "not": true}],
          "color": {
            "field": "Stain",
            "type": "nominal",
            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
            "range": [
              "white",
              "#D9D9D9",
              "#979797",
              "#636363",
              "black",
              "#A0A0F2"
            ]
          }
        },
        {
          "mark": "triangleRight",
          "dataTransform": [
              {"type":"filter", "field": "Stain", "oneOf": ["acen"]},
              {"type":"filter", "field": "Name", "include": "q"}
            ],
          "color": {"value": "#B40101"}
        },
        {
          "mark": "triangleLeft",
          "dataTransform": [
              {"type":"filter", "field": "Stain", "oneOf": ["acen"]},
              {"type":"filter", "field": "Name", "include": "p"}
            ],
          "color": {"value": "#B40101"}
        }
      ],
      "size": {"value": 20},
      "stroke": {"value": "gray"},
      "strokeWidth": {"value": 0.5}
    }
  ]
}
```


## Circular Layout

We can easily turn the visualization into a circular layout through the `layout` property.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/tutorial/tutorial_circular.png" alt="gosling circular" width="600"/>

```diff
+ "layout": "circular",
+ "centerRadius": 0.6,
```

<details>
<summary><b>Click here to expand the complete code</b></summary>

```javscript
{
  "layout": "circular",
  "centerRadius": 0.6,
  "spacing": 5,  
  "tracks": [
     { 
      "width": 700,
      "height": 40,  
      "data": {
        "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
        "type": "multivec",
        "row": "sample",
        "column": "position",
        "value": "peak",
        "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
      },
      "mark": "area",
      "x": {
        "field": "position",
        "type": "genomic",
        "domain": {"chromosome": "1"},
        "axis": "top",
        "linkingId": "link-1"
      },
      "y": {"field": "peak", "type": "quantitative"},
      "color": {"field": "sample", "type": "nominal"}
    },
    { 
      "width": 700,
      "height": 20,  
      "data": {
        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
        "type": "csv",
        "chromosomeField": "Chromosome",
        "genomicFields": ["chromStart", "chromEnd"]
      },
      "x": {
        "field": "chromStart",
        "type": "genomic",
        "domain": {"chromosome": "1"},
        "linkingId": "link-1"
      },
      "xe": {"field": "chromEnd", "type": "genomic"},
      "alignment": "overlay",
      "tracks": [
        {
          "mark": "text",
          "dataTransform": [{"type":"filter", "field": "Stain", "oneOf": ["acen"], "not": true}],
          "text": {"field": "Name", "type": "nominal"},
          "color": {
            "field": "Stain",
            "type": "nominal",
            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
            "range": ["black", "black", "black", "black", "white", "black"]
          },
          "visibility": [
            {
              "operation": "less-than",
              "measure": "width",
              "threshold": "|xe-x|",
              "transitionPadding": 10,
              "target": "mark"
            }
          ],
          "style": {"textStrokeWidth": 0}
        },
        {
          "mark": "rect",
          "dataTransform": [{"type":"filter", "field": "Stain", "oneOf": ["acen"], "not": true}],
          "color": {
            "field": "Stain",
            "type": "nominal",
            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
            "range": [
              "white",
              "#D9D9D9",
              "#979797",
              "#636363",
              "black",
              "#A0A0F2"
            ]
          }
        },
        {
          "mark": "triangleRight",
          "dataTransform": [
              {"type":"filter", "field": "Stain", "oneOf": ["acen"]},
              {"type":"filter", "field": "Name", "include": "q"}
            ],
          "color": {"value": "#B40101"}
        },
        {
          "mark": "triangleLeft",
          "dataTransform": [
              {"type":"filter", "field": "Stain", "oneOf": ["acen"]},
              {"type":"filter", "field": "Name", "include": "p"}
            ],
          "color": {"value": "#B40101"}
        }
      ],
      "size": {"value": 20},
      "stroke": {"value": "gray"},
      "strokeWidth": {"value": 0.5}
    }
  ]
}
```
</details>
