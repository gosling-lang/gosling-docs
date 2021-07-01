---
title: Multi-view Visualizations
---
In [Tutorial 2](https://github.com/gosling-lang/gosling-docs/blob/master/tutorials/create-multi-track-visualization.md), we introduce how to create a multi-track visualization, as shown below.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/tutorial/tutorial_circular.png" alt="gosling circular" width="600"/>

<details>
<summary><b>Click here to expand the complete code</b></summary>

```javascript
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
          "dataTransform":  [{"type":"filter", "field": "Stain", "oneOf": ["acen"], "not": true}],
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

In Gosling, we call a visualization with several `tracks` as **a single view**.
Sometimes, we may wish to create a visualization with **multiple views**, e.g., one overview + several detailed views.

## create Multiple Views

Let's say we use the above circular visualization as the overview that visualizes all the chromosomes. 
To achieve this, we remove the specified `x.domain` in the overview.
**Overview**
```diff
-  "domain": {"chromosome": "1"},
```

We then create two linear detailed views for two different chromosomes, e.g., chromosome 2 and chromosome 5.


**Detailed View 1**

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/tutorial/tutorial_detail_view1.png" alt="gosling detailed view 1" width="340"/>

```diff
+   {
+     "layout": "linear",
+     "tracks": [{ 
+       "row": {"field": "sample", "type": "nominal"},
+       "width": 340,
+       "height": 300,  
+       "data": {
+         "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
+         "type": "multivec",
+         "row": "sample",
+         "column": "position",
+         "value": "peak",
+         "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
+       },
+       "mark": "area",
+       "x": {
+         "field": "position",
+         "type": "genomic",
+         "domain": {"chromosome": "2"}
+         "axis": "top"
+       },
+       "y": {"field": "peak", "type": "quantitative"},
+       "color": {"field": "sample", "type": "nominal"}
+   }]
+   }
```



**Detailed View 2** is the same as **Detailed View 1** except the `x.domain`.

```diff
-  "domain": {"chromosome": "2"}
+  "domain": {"chromosome": "5"}
```
<details>
<summary>Click to expand the complete code for Detailed View 2</summary>

```diff
+   {
+     "layout": "linear",
+     "tracks": [{ 
+       "row": {"field": "sample", "type": "nominal"},
+     "width": 340,
+     "height": 300,  
+     "data": {
+       "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
+       "type": "multivec",
+       "row": "sample",
+       "column": "position",
+       "value": "peak",
+       "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
+     },
+     "mark": "area",
+     "x": {
+       "field": "position",
+       "type": "genomic",
+       "domain": {"chromosome": "5"}
+       "axis": "top"
+     },
+     "y": {"field": "peak", "type": "quantitative"},
+     "color": {"field": "sample", "type": "nominal"}
+   }]
+   }
```
</details>


## Arrange Multiple Views
So far, we have created one overview and two detailed views.
In Gosling, multiple views can be arranged using the `arrangement` property.

```javascript
{
    "arrangement": "parallel"
    "views": [
        {/** overview **/},
        {
            "arrangement": "serial",
            "spacing": 20,
            "views": [
                {/** detailed view 1 **/},
                {/** detailed view 2 **/}
            ]
        }
    ]
}
```

<details>
<summary><b>Click here to expand the complete code</b></summary>

```javascript
{
    "arrangement": "vertical",
    "views": [
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
                        "categories": [
                            "sample 1",
                            "sample 2",
                            "sample 3",
                            "sample 4"
                        ]
                    },
                    "mark": "area",
                    "x": {
                        "field": "position",
                        "type": "genomic",
                        "axis": "top",
                        "linkingId": "link-1"
                    },
                    "y": {
                        "field": "peak",
                        "type": "quantitative"
                    },
                    "color": {
                        "field": "sample",
                        "type": "nominal"
                    },
                    "alignment": "overlay",
                    "tracks": [
                        {
                            "mark": "area"
                        },
                        {
                            "mark": "brush",
                            "x": {
                                "linkingId": "detail-1"
                            },
                            "color": {
                                "value": "blue"
                            }
                        },
                        {
                            "mark": "brush",
                            "x": {
                                "linkingId": "detail-2"
                            },
                            "color": {
                                "value": "red"
                            }
                        }
                    ]
                },
                {
                    "width": 700,
                    "height": 20,
                    "data": {
                        "url": "https://raw.githubusercontent.com/sehilyi/gemini-datasets/master/data/UCSC.HG38.Human.CytoBandIdeogram.csv",
                        "type": "csv",
                        "chromosomeField": "Chromosome",
                        "genomicFields": [
                            "chromStart",
                            "chromEnd"
                        ]
                    },
                    "x": {
                        "field": "chromStart",
                        "type": "genomic"
                    },
                    "xe": {
                        "field": "chromEnd",
                        "type": "genomic"
                    },
                    "alignment": "overlay",
                    "tracks": [
                        {
                            "mark": "text",
                            "dataTransform": [
                                    {
                                        "type":"filter", 
                                        "field": "Stain",
                                        "oneOf": [
                                            "acen"
                                        ],
                                        "not": true
                                    }
                                ],
                            "text": {
                                "field": "Name",
                                "type": "nominal"
                            },
                            "color": {
                                "field": "Stain",
                                "type": "nominal",
                                "domain": [
                                    "gneg",
                                    "gpos25",
                                    "gpos50",
                                    "gpos75",
                                    "gpos100",
                                    "gvar"
                                ],
                                "range": [
                                    "black",
                                    "black",
                                    "black",
                                    "black",
                                    "white",
                                    "black"
                                ]
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
                            "style": {
                                "textStrokeWidth": 0
                            }
                        },
                        {
                            "mark": "rect",
                            "dataTransform": [
                                    {
                                        "type":"filter", 
                                        "field": "Stain",
                                        "oneOf": [
                                            "acen"
                                        ],
                                        "not": true
                                    }
                                ],
                            "color": {
                                "field": "Stain",
                                "type": "nominal",
                                "domain": [
                                    "gneg",
                                    "gpos25",
                                    "gpos50",
                                    "gpos75",
                                    "gpos100",
                                    "gvar"
                                ],
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
                                    {
                                        "type":"filter", 
                                        "field": "Stain",
                                        "oneOf": [
                                            "acen"
                                        ]
                                    },
                                    {
                                        "type":"filter", 
                                        "field": "Name",
                                        "include": "q"
                                    }
                                ],
                            "color": {
                                "value": "#B40101"
                            }
                        },
                        {
                            "mark": "triangleLeft",
                            "dataTransform": [
                                    {
                                        "type":"filter", 
                                        "field": "Stain",
                                        "oneOf": [
                                            "acen"
                                        ]
                                    },
                                    {
                                        "type":"filter", 
                                        "field": "Name",
                                        "include": "p"
                                    }
                                ],
                            "color": {
                                "value": "#B40101"
                            }
                        }
                    ],
                    "size": {
                        "value": 20
                    },
                    "stroke": {
                        "value": "gray"
                    },
                    "strokeWidth": {
                        "value": 0.5
                    }
                }
            ]
        },
        {
            "arrangement": "serial",
            "spacing": 100,
            "views": [
                {
                    "layout": "linear",
                    "tracks": [
                        {
                            "row": {
                                "field": "sample",
                                "type": "nominal"
                            },
                            "width": 300,
                            "height": 100,
                            "data": {
                                "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
                                "type": "multivec",
                                "row": "sample",
                                "column": "position",
                                "value": "peak",
                                "categories": [
                                    "sample 1",
                                    "sample 2",
                                    "sample 3",
                                    "sample 4"
                                ]
                            },
                            "mark": "area",
                            "x": {
                                "field": "position",
                                "type": "genomic",
                                "domain": {
                                    "chromosome": "2"
                                },
                                "axis": "top"
                            },
                            "y": {
                                "field": "peak",
                                "type": "quantitative"
                            },
                            "color": {
                                "field": "sample",
                                "type": "nominal"
                            }
                        }
                    ]
                },
                {
                    "layout": "linear",
                    "tracks": [
                        {
                            "row": {
                                "field": "sample",
                                "type": "nominal"
                            },
                            "width": 300,
                            "height": 100,
                            "data": {
                                "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
                                "type": "multivec",
                                "row": "sample",
                                "column": "position",
                                "value": "peak",
                                "categories": [
                                    "sample 1",
                                    "sample 2",
                                    "sample 3",
                                    "sample 4"
                                ]
                            },
                            "mark": "area",
                            "x": {
                                "field": "position",
                                "type": "genomic",
                                "domain": {
                                    "chromosome": "5"
                                },
                                "axis": "top"
                            },
                            "y": {
                                "field": "peak",
                                "type": "quantitative"
                            },
                            "color": {
                                "field": "sample",
                                "type": "nominal"
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
```
</details>


## Link Multiple Views
We need to link the overview and the two detailed views.
We overlay two `brush` objects to the overview, and link the two `brush` objects to the two detailed views using `linkingId` (i.e., "detail-1", "detail-2").
To help users visually link the brush objects and the detailed views, we assign the same color to the `brush` of the overview and the `background` of the corresponding detailed view.

**Overview**
```diff
+ "alignment": "overlay",
+ "tracks": [
+    {
+        "mark": "area"
+    },
+    {
+        "mark": "brush",
+        "x": {
+            "linkingId": "detail-1"
+        },
+        "color": {
+            "value": "blue"
+        }
+    },
+    {
+        "mark": "brush",
+        "x": {
+            "linkingId": "detail-2"
+        },
+        "color": {
+            "value": "red"
+        }
+    }
+ ]
```

**Detailed View 1**
```diff
+  "linkingId": "detail-1",

+  "style": {
+     "background": "blue",
+     "backgroundOpacity": 0.1
+  }
```

**Detailed View 2**
```diff
+  "linkingId": "detail-2",

+  "style": {
+     "background": "red",
+     "backgroundOpacity": 0.1
+  }
```

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/tutorial/tutorial_multi_views.gif" alt="gosling linked multi-views" width="600"/>

<details>
<summary><b>Click here to expand the complete code</b></summary>

```javascript
{
    "arrangement": "vertical",
        "views": [
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
                            "axis": "top",
                            "linkingId": "link-1"
                        },
                        "y": { "field": "peak", "type": "quantitative" },
                        "color": { "field": "sample", "type": "nominal" },
                        "alignment": "overlay",
                        "tracks": [
                            { "mark": "area" },
                            {
                                "mark": "brush",
                                "x": { "linkingId": "detail-1" },
                                "color": { "value": "blue" }
                            },
                            {
                                "mark": "brush",
                                "x": { "linkingId": "detail-2" },
                                "color": { "value": "red" }
                            }
                        ]
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
                            "linkingId": "link-1"
                        },
                        "xe": { "field": "chromEnd", "type": "genomic" },
                        "alignment": "overlay",
                        "tracks": [
                            {
                                "mark": "text",
                                "dataTransform": [{"type":"filter",  "field": "Stain", "oneOf": ["acen"], "not": true }],
                                "text": { "field": "Name", "type": "nominal" },
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
                                "style": { "textStrokeWidth": 0 }
                            },
                            {
                                "mark": "rect",
                                "dataTransform": [{"type":"filter", "field": "Stain", "oneOf": ["acen"], "not": true }],
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
                                        {"type":"filter", "field": "Stain", "oneOf": ["acen"] },
                                        {"type":"filter", "field": "Name", "include": "q" }
                                    ],
                                "color": { "value": "#B40101" }
                            },
                            {
                                "mark": "triangleLeft",
                                "dataTransform":  [
                                        {"type":"filter", "field": "Stain", "oneOf": ["acen"] },
                                        {"type":"filter", "field": "Name", "include": "p" }
                                    ],
                                "color": { "value": "#B40101" }
                            }
                        ],
                        "size": { "value": 20 },
                        "stroke": { "value": "gray" },
                        "strokeWidth": { "value": 0.5 }
                    }
                ]
            },
            {
                "arrangement": "serial",
                "spacing": 20,
                "views": [
                    {
                        "layout": "linear",
                        "tracks": [
                            {
                                "row": { "field": "sample", "type": "nominal" },
                                "width": 340,
                                "height": 300,
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
                                    "domain": { "chromosome": "2" },
                                    "linkingId": "detail-1",
                                    "axis": "top"
                                },
                                "y": { "field": "peak", "type": "quantitative" },
                                "color": { "field": "sample", "type": "nominal" },
                                "style": { "background": "blue", "backgroundOpacity": 0.1 }
                            }
                        ]
                    },
                    {
                        "layout": "linear",
                        "tracks": [{
                            "row": { "field": "sample", "type": "nominal" },
                            "width": 340,
                            "height": 300,
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
                                "domain": { "chromosome": "5" },
                                "linkingId": "detail-2",
                                "axis": "top"
                            },
                            "y": { "field": "peak", "type": "quantitative" },
                            "color": { "field": "sample", "type": "nominal" },
                            "style": { "background": "red", "backgroundOpacity": 0.1 }
                        }]
                    }
                ]
            }
        ]
}
```
</details>