In the [first tutorial](https://github.com/gosling-lang/gosling.js/wiki/Tutorial), we introduce how to load data, encode data with marks, transform data, superpose multiple marks and obtain the following visualization.
<img src="https://raw.githubusercontent.com/wiki/gosling-lang/gosling.js/images/tutorial_superpose.png" alt="gosling vis superpose" width="800"/>
<details>
  <summary>click to expand the code</summary>

```javascript
{
    "arrangement": {"rowSizes": 70, "columnSizes": 700 },
    "tracks":[{
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
        "size": {"value": 20},
        "superpose":[
             {
             "mark": "rect",
             "dataTransform": {
                     "filter": [{"field": "Stain", "oneOf": ["acen"], "not": true}]
                 },
             "color": {
                 "field": "Stain", 
                 "type": "nominal",
                 "domain": ["gpos25", "gpos50", "gpos75", "gpos100"],
                 "range": ["#D9D9D9","#979797","#636363", "black"]
             }
             },
            {
              "mark": "triangle-r",
              "dataTransform": {
                "filter": [
                  {"field": "Stain", "oneOf": ["acen"]},
                  {"field": "Name", "include": "q"}
                ]
              },
              "color": {"value": "#B70101"}
            },
            {
              "mark": "triangle-l",
              "dataTransform": {
                "filter": [
                  {"field": "Stain", "oneOf": ["acen"]},
                  {"field": "Name", "include": "p"}
                ]
              },
              "color": {"value": "#B70101"}
            }
        ],
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

[Semantic zoom](https://github.com/gosling-lang/gosling.js/wiki/Documentation#semantic-zooming) allows users to switch between different visualizations of the same data through zooming in/out. When zooming in, the same data will be represented in a different way in which more details are shown. 

Let's say, for this visualization, we want text annotations to show up when zooming in.
We add `text` marks to the `superpose` property and specify when the `text` marks should appear through the `visibility` property.
We may wish the text marks to appear when the distance between chromStart and chromEnd is big enough to place a text mark.
In other words, the text marks appear when the width (`measure`) of the text mark (`target`) is less than (`operation`) than `|xe-x|`.

```diff
{
  "arrangement": {
    "columnSizes": 700, 
    "rowSizes": 70
  },
  "tracks": [
    {
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
      "size": {"value": 20},
      "superpose": [
+        {
+          "mark": "text",
+          "dataTransform": {
+            "filter": [{"field": "Stain", "oneOf": ["acen"], "not": true}]
+          },
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
          "dataTransform": {
            "filter": [{"field": "Stain", "oneOf": ["acen"], "not": true}]
          },
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
      "stroke": {"value": "gray"},
      "strokeWidth": {"value": 0.5}
    }
  ]
}
```

<img src="https://raw.githubusercontent.com/wiki/gosling-lang/gosling.js/images/tutorial_text_label.png" alt="gosling semantic zoom" width="800"/>

## Multiple Linked Tracks

We may wish to add another track to the `tracks` to represent the same data from different aspects.
These two tracks share the same `x` coordinate. As a result, we link these two tracks by assigning them the same  `linkingID`. The zooming and panning performed in one track will be automatically applied to the linked track.  

```diff
{
  "arrangement": {
    "columnSizes": 700, 
-    "rowSizes": [70], 
+    "rowSizes": [70, 25]
  },
  "tracks": [
+     {
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
+        "linkingID": "link-1"
+      },
+      "y": {"field": "peak", "type": "quantitative"},
+      "color": {"field": "sample", "type": "nominal"}
+    },
    {
      "data": {
        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
        "type": "csv",
        "chromosomeField": "Chromosome",
        "genomicFields": ["chromStart", "chromEnd"]
      },
      ,
      "x": {
        "field": "chromStart",
        "type": "genomic",
        "domain": {"chromosome": "1"},
-        "axis": "top"
+        "linkingID": "link-1"
      },
      "xe": {"field": "chromEnd", "type": "genomic"},
      "size": {"value": 20},
      "superpose": [
        {
          "mark": "text",
          "dataTransform": {
            "filter": [{"field": "Stain", "oneOf": ["acen"], "not": true}]
          },
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
          "dataTransform": {
            "filter": [{"field": "Stain", "oneOf": ["acen"], "not": true}]
          },
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
      "stroke": {"value": "gray"},
      "strokeWidth": {"value": 0.5}
    }
  ]
}
```

<img src="https://raw.githubusercontent.com/wiki/gosling-lang/gosling.js/images/tutorial_multi_track.png" alt="gosling multi tracks" width="800"/>

## Circular Layout

We can easily turn the visualization into a circular layout through the `layout` property.
The size of each track is specified by `innerRadius` and `outerRadius`. We can also stack these two tracks together by setting `superposeOnPreviousTrack` as true.

```diff
{
+ "layout": "circular",
  "arrangement": {
-     "columnSizes": 800,
-    "rowSizes": [60, 25], 
+    "columnSizes": 600,
+    "rowSizes": 600
  },
  "tracks": [
     {
+      "innerRadius": 200,
+      "outerRadius": 300,
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
        "linkingID": "link-1"
      },
      "y": {"field": "peak", "type": "quantitative"},
      "color": {"field": "sample", "type": "nominal"}
    },
    {
+      "innerRadius": 175,
+      "outerRadius": 200,
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
        "linkingID": "link-1"
      },
      "xe": {"field": "chromEnd", "type": "genomic"},
      "size": {"value": 20},
      "superpose": [
        {
          "mark": "text",
          "dataTransform": {
            "filter": [{"field": "Stain", "oneOf": ["acen"], "not": true}]
          },
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
          "dataTransform": {
            "filter": [{"field": "Stain", "oneOf": ["acen"], "not": true}]
          },
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
      "stroke": {"value": "gray"},
      "strokeWidth": {"value": 0.5},
+      "superposeOnPreviousTrack": true
    }
  ]
}
```

<img src="https://raw.githubusercontent.com/wiki/gosling-lang/gosling.js/images/tutorial_circular.png" alt="gosling circular" width="600"/>