Gosling is a declarative visualization grammar tailored for interactive genomic visualizations. In Gosling, users can create visualizations through a JSON syntax. This documentation describes how to write the JSON specification to create interactive visualizations.
You are welcome to try the [Gosling online editor](https://gosling-lang.github.io/gosling.js/)!

```javascript
// Gosling generates visualizations through a JSON specification language

{
  // each track represent a single visualization
  "tracks":[
    {
      // specify the data source and data format of this track
      "data": {
        "url": ...,
        "type":...
      },
      // specify the mark types and visual encodings
      "mark": ...,
      "x": ...,
      ...
    },
    {
      ... // another track
    },
    ...
  ],
  // specify the arrangement of multiple tracks
  "arrangement":{
    ...
  }
}
```

# List of Contents
- [Genome Build](https://github.com/gosling-lang/gosling.js/wiki/Genome-Builds)
- [Data](https://github.com/gosling-lang/gosling.js/wiki/Data)
  - [CSV](https://github.com/gosling-lang/gosling.js/wiki/Data#csv)
  - [JSON](https://github.com/gosling-lang/gosling.js/wiki/Data#json)
  - [BigWig](https://github.com/gosling-lang/gosling.js/wiki/bigwig)
  - [Vector](https://github.com/gosling-lang/gosling.js/wiki/Data#vector)
  - [Multivec](https://github.com/gosling-lang/gosling.js/wiki/Data#multivec)
  - [BED](https://github.com/gosling-lang/gosling.js/wiki/Data#bed)
  - [Data Transform](https://github.com/gosling-lang/gosling.js/wiki/Data#data-transform)
- [Mark](https://github.com/gosling-lang/gosling.js/wiki/Mark)
  - [Point](https://github.com/gosling-lang/gosling.js/wiki/Mark#point)
  - [Line](https://github.com/gosling-lang/gosling.js/wiki/Mark#line)
  - [Area](https://github.com/gosling-lang/gosling.js/wiki/Mark#area)
  - [Bar](https://github.com/gosling-lang/gosling.js/wiki/Mark#bar)
  - [Rect](https://github.com/gosling-lang/gosling.js/wiki/Mark#rect)
  - [Text](https://github.com/gosling-lang/gosling.js/wiki/Mark#text)
  - [Link](https://github.com/gosling-lang/gosling.js/wiki/Mark#link)
  - [Triangle](#triangle)
- [Visual Channel](#visual-channels-of-mark)
  - [x](#x)
  - [xe](#xe)
  - [y](#y)
  - [ye](#ye)
  - [x1 x1e y1 y1e](#x1-x1e-y1-y1e)
  - [row](#row)
  - [size](#size)
  - [text](#text-1)
  - [color](#color)
  - [stroke](#stroke)
  - [strokeWidth](#strokewidth)
  - [opacity](#opacity)
  - [Style](https://github.com/gosling-lang/gosling.js/wiki/Track#style)
- [Tracks](https://github.com/gosling-lang/gosling.js/wiki/Track)
  - [Layout](https://github.com/gosling-lang/gosling.js/wiki/Track#layout)
  - [Arrangement](https://github.com/gosling-lang/gosling.js/wiki/Track#arrangement)
    - [Grid-based arrangement](https://github.com/gosling-lang/gosling.js/wiki/Track#grid-based-arrangement)
    - [Superposition](https://github.com/gosling-lang/gosling.js/wiki/Track#superposition)
- [Interactions](https://github.com/gosling-lang/gosling.js/wiki/User-Interaction)
  - [Zooming and Panning](https://github.com/gosling-lang/gosling.js/wiki/User-Interaction#zooming-and-panning)
  - [Linking Views](https://github.com/gosling-lang/gosling.js/wiki/User-Interaction#linking-views)
  - [Brushing and Linking](https://github.com/gosling-lang/gosling.js/wiki/User-Interaction#brushing-and-linking)
  - [Semantic Zooming](https://github.com/gosling-lang/gosling.js/wiki/User-Interaction#semantic-zooming)