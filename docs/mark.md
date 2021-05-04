---
title: Mark
---
Visual marks (e.g., points, lines, and bars) are the basic graphical elements of a visualization. Note here that we call one visualization a `track` in Gosling.
The core of constructing a visualization is to bind selected **data fields** to the **visual channels** (e.g., size, color, and position) of a chosen **mark type**.

The `mark` property of a track is defined by a string that describes the mark type.
```javascript
{
    "tracks":[
      {
        "mark": "rect",
        ... // other track properties
      },
      {
        "mark": "line",
        ... // other track properties
      }
    ],
    ... // other visualization properties
}
```
Gosling supports the following primitive `mark` types: `point`, `line`, `area`, `bar`, `rect`, `text`, `link`, `rule`, `triangle`. Composite mark (i.e., glyph) is also supported through the [`alignment`](https://github.com/gosling-lang/gosling-docs/blob/master/docs/composition.md#overlaid-tracks)) property.

- [Point](#point)
- [Line](#line)
- [Area](#area)
- [Bar](#bar)
- [Rect](#rect)
- [Text](#text)
- [Link](#link)
- [Triangle](#triangle)

## Point
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/master/src/core/mark/point.ts)

The mark `point` represents one data point using a circular shape. Visual channels of the circle, such as radius, color, and vertical/horizontal position, are used to represent values of the data point. Popular charts such as scatter plots and bubble charts use `point` mark.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/point_example.png" width="800" alt="point_example"/>  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/e7ed2a61336b0ecc40211c8c3004388a>)

```javascript
// an example of point marks
{
    "tracks":[{
        "data": {
            "url": ...,
            "type": ...
        },
        // mark type
        "mark": "point",
        // mark visual channels
        "x": {
            "field": "position", // data field
            "type": "genomic", // type of data field
            "axis": "top"
        },
        "y": {
            "field": "peak", 
            "type": "quantitative"
        },
        ... // other encodings and styles
    }]
}
```
## Line

The mark `line` represents a set of data points using a line that connects these points.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/line_example.png" width="800" alt="line_example"/>  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/12e9bc738ed19d325a900ff50d1f85dc>)

```javascript
// an example of using line marks
{
    "tracks":[{
        "data": {
            "url": ...,
            "type": ...
        },
        // specify mark type
        "mark": "line",
        // specify mark visual channels
        "x": {
            "field": "position", // data field
            "type": "genomic", // type of data field
            "axis": "top" // position of the x axis 
        },
        "y": {
            "field": "peak", 
            "type": "quantitative"
        },
        ... // other encodings and styles
    }]
}
```
## Area
The mark `area` represents a set of data points as an area shape. The upper edge of the area shape is a line that connects all the points and the bottom edge is the x axis.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/area_example.png" width="800" alt="area_example"/>  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/213dcc25c61427bef243baefd8c36801>)

```javascript
// an example of area marks
{
    "tracks":[{
        "data": {
            "url": ...,
            "type": ...
        },
        // mark type
        "mark": "area",
        // mark visual channels
        "x": {
            "field": "position", // data field
            "type": "genomic", // type of data field
            "axis": "top"
        },
        "y": {
            "field": "peak", 
            "type": "quantitative"
        },
        "color": ...,
        ... // other encodings and styles
    }]
}
```

## Bar

The `bar` mark is designed for drawing bar charts. Each bar shows the value of one data point through its height.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/bar_example.png" width="800" alt="bar_example"/>  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/3acca936d08e676c9a274de73d094492>)

```javascript
// an example of area marks
{
    "tracks":[{
        "data": {
            "url": ...,
            "type": ...
        },
        // mark type
        "mark": "bar",
        // mark visual channels
        "x": {
            "field": "position", // data field
            "type": "genomic", // type of data field
            "axis": "top"
        },
        // y indicates the visual encoding of the bar height
        "y": {
            "field": "peak", 
            "type": "quantitative"
        },
        ... // other encodings and styles
    }]
}
```

## Rect
The `rect` mark is designed for representing genomic intervals using rectangular shapes. Left and right edge of the rectangle indicate the start and end genomic positions, respectively.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/rect_example.png" width="800" alt="rect_example"/>  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/a5399812193a29fe7c85c519869a42ca>)

```javascript
// an example of rect marks
{
    "traks":[
    {
        "data": ...,
        // specify the type of mark
        "mark": "rect", 
        // bind the color of each rect mark to the data field: Stain
        "color": { 
            "field": "Stain",
            "type": "nominal",,
            "domain": ["gneg", "gpos25", "gpos50", "gpos75", "gpos100", "gvar"],
            "range": ["white", "#D9D9D9", "#979797", "#636363", "black", "#A0A0F2"]
          },
        // bind the start position of each rect mark to the data field: chromStart 
        "x": { 
            "field": "chromStart",
            "type": "genomic",
            "axis": "top"
        },
        // bind the end position of each rect mark to the data field: chromEnd 
        "xe": { 
            "field": "chromEnd", "type": "genomic"
        },
        "size": {
            "value": 30 // specify the constant height of each rect mark
        }
    }, 
    ... // other encodings and styles of the rect mark
    ],
}

```

## Text

The `text` mark is designed to display textual labels. For example, gene names and nucleobases can be displayed with `text` marks.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/text_example.png" width="800" alt="text_example"/>  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/3a3c7fce17876e6ef879d1aa499a4664>)

```javascript
{
    "tracks":[{
      "data": ...,
      
      // specify the type of mark
      "mark": "text", 
      
      // specify styles of the mark
      "style": {"textStrokeWidth": 0},

      // bind visual channels to corresponding data fields
      "x": {"field": "start", "type": "genomic", "axis": "top"},
      "xe": {"field": "end", "type": "genomic"},
      "y": {"field": "count", "type": "quantitative"},
      "color": {
        "field": "base",
        "type": "nominal",
        "domain": ["A", "T", "G", "C"]
      },

      // specify the text content
      "text": {"field": "base", "type": "nominal"} 
    }]
}
```

## Link

The `link` mark is designed to show connections between chromosomes using an arc that connects two genomic intervals.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/link_example.png" width="800" alt="link_example"/>  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/6f96c2418016d963f3eb071adba31c56>)


```javascript
{
  "tracks": [
      {
        "data": ...,

        "mark": "link", // specify the mark type

        // bind visual channels to corresponding data fields

        // x and xe indicates the start point of the arc  
        "x": {
          "field": "s1",
          "type": "genomic",
          "domain": {"chromosome": "1"},
          "axis": "top"
        },
        "xe": {"field": "e1", "type": "genomic"},

        // x and xe indicates the end point of the arc  
        "x1": {
          "field": "s2",
          "type": "genomic",
          "domain": {"chromosome": "1"},
          "axis": "top"
        },
        "x1e": {"field": "e2", "type": "genomic"},

        // specify styles of the mark
        "stroke": {"value": "steelblue"},
        "style": {"circularLink": true}
      }
    ]
}
```

## Triangle

[:link: source code](https://github.com/gosling-lang/gosling.js/blob/master/src/core/mark/triangle.ts)  

Gosling supports three types of triangle marks: `triangleLeft`, `triangleRight`, `triangleBottom`