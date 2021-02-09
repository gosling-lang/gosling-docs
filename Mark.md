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
Gosling supports the following primitive `mark` types: `point`, `line`, `area`, `bar`, `rect`, `text`, `link`, `rule`, `triangle`. Composite mark (i.e., glyph) is also supported through the [`superpose`](#superposition) property.

[:link: source code](https://github.com/gosling-lang/gosling.js/blob/master/src/core/mark)

### Point
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/master/src/core/mark/point.ts)

The mark `point` represents one data point using a circular shape. Visual channels of the circle, such as radius, color, and vertical/horizontal position, are used to represent values of the data point. Popular charts such as scatter plots and bubble charts use `point` mark.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/point_example.png" width="800" alt="point_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(6'ZtleJBasic%20Marks%3A%20Point'NsubZtleJTutorial%20ExOs'NlayoutJlinear'Narrangement4('direcZonJverZcal'G'rowSizes4180G'columnSizes4800)Ntracks4%5B6*(K'~'urlJhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2FZleset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQXIZleset'Kjmeta~Ihiglass-mulZvecX'rowJsOX'columnJposiZonX'valueJpeakX'categories4%5B'sO%201'%5DKjmarkJpoint'2'x4(K*WposiZonXIgenomicX'domain4('chromosomeJ1'G'interval4%5B1G3000500%5D)2*'axisJtop'Kjy4Csize4Ccolor4(WsO'GInominal'G'legend4truejopacity4('value40.9)6*)6%5D%0A)*%20%202%2CK4!%206%0A*C(Wpeak'GIquanZtaZve'jG%2C%20I'typeJJ4'K6**N%2C6'OampleW'fieldJX'2*Ztij)2'~data4(K*%01~jZXWONKJIGC642*_>)

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
### Line

The mark `line` represents a set of data points using a line that connects these points.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/line_example.png" width="800" alt="line_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(9'NtleJBasic%20Marks%3A%20Line'4'subNtleJTutorial%20ExWs'4'layoutJlinear'4'arrangement~direcNonJverNcal'G'rowSizes6180G'columnSizes6800)4'tracksj9*(9CdataXurlJhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2FNleset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQIKNleset'OmetadataXKhiglass-mulNvecIrowJsWIcolumnZvalueJpeakIcategoriesj'sW%201'%5DOmarkJline'4CxXfieldZKgenomicIdomain~chromosomeJ1'G'intervalj1G3000500%5D)4*CaxisJbottom'Oy~fieldJpeak'G'KquanNtaNve')4Csize~value62)9*)9%5D%0A)*%20%204%2C96!%209%0A*C**'G%2C%20I'4*CJ6'KtypeJNtiO9**)4CWampleX6(9*CZJposiNonIj6%5B~6('%01~jZXWONKJIGC964*_>)

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
### Area
The mark `area` represents a set of data points as an area shape. The upper edge of the area shape is a line that connects all the points and the bottom edge is the x axis.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/area_example.png" width="800" alt="area_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(9'NtleJBasic%20Marks%3A%20Area'4'subNtleJTutorial%20ExWs'4'layoutJlinear'4'arrangement6('direcNonJverNcal'G'rowSiz~6180G'columnSiz~6800)4'tracksj9*(9CdataXurlJhttps%3A%2F%2Fr~gen.io%2Fapi%2Fv1%2FNl~et_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQIKNl~et'OmetadataXKhiglass-mulNvecIrowJsWIcolumnZvalueJpeakIcategori~j'sW%201'%5DOmarkJarea'4CxXfieldZKgenomicIdomain6('chromosomeJ1'G'intervalj2000500G3000500%5D)4*CaxisJbottom'Oy6('fieldJpeak'G'KquanNtaNve')9*)9%5D%0A)*%20%204%2C96!%209%0A*C**'G%2C%20I'4*CJ6'KtypeJNtiO9**)4CWampleX6(9*CZJposiNonIj6%5B~es%01~jZXWONKJIGC964*_>)

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

### Bar

The `bar` mark is designed for drawing bar charts. Each bar shows the value of one data point through its height.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/bar_example.png" width="800" alt="bar_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(C'OtleKBasic%20Marks%3A%20Bar'4'subOtleKTutorial%20ExXs'4'layoutKlinear'4'arrangement6('direcOonKverOcal'I'rowSizes6180I'columnSizes6800)4'tracks~C*(CGdataZurlKhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2FOleset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQJNOleset'WmetadataZNhiglass-mulOvecJrowKsXJcolumnjvalueKpeakJcategories~'sX%201'%5DWmarkKbar'4GxZfieldjNgenomicJdomain6('chromosomeK1'I'interval~2900500I3000500%5D)4*GaxisKbottom'Wy6('fieldKpeak'I'NquanOtaOve')C*)C%5D%0A)*%20%204%2CC6!%20C%0A*G**'I%2C%20J'4*GK6'NtypeKOtiWC**)4GXampleZ6(C*GjKposiOonJ~6%5B%01~jZXWONKJIGC64*_>)

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

### Rect
The `rect` mark is designed for representing genomic intervals using rectangular shapes. Left and right edge of the rectangle indicate the start and end genomic positions, respectively.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/rect_example.png" width="800" alt="rect_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(K%20'titleZBasic%20Marks%3A%20Rect'_'subtitleZTutorial%20Examples'_'layoutZlinear'_'arrangementJ(K*'directionZvertical'_*'columnSizesJ800_*'rowSizesX60L180L180L180%5DK)_'tracksXK*(Q'dataJ(KNurlZhttps%3A%2F%2Fraw.githubusercontent.com%2Fsehilyi%2Fgemini-datasets%2Fmaster%2Fdata%2FUCSC.HG38.Human.CytoBandIdeogram.csvV'~csvVPosomeFjZChromosomeV'%22FjsXPStart'LPEnd'%5DQ)4K*NmarkZrectV*'dataTransformJ(QNfilterX('fjZStain'L'oneOfX'acen'%5DL'notJtrue)%5DQ**)4**'colorJ(QNfjZStain'4N~nominal'4NdomainX'gnegY25Y50Y75Y100'L'gvar'%5D4NrangeXQ*NwhiteVN%23D9D9D9VN%23979797VN%23636363VNblackVN%23A0A0F2'Q***%5DQ**)Q*4'xJ(KNfjJPStartV'~%22V'domainJ(PosomeZ1')4*'axisZtop'Q)4'xeJ('fjJPEnd'L'~%22')4'sizeqJ20)4'strokeqZgray')4'strokeWidthqJ0.5)4'styleJ('outlineZwhite')K*)K%5D%0A)*%20%204%2CQJ!%20K%0A*L%2C%20N***'P'chromQK**V'4*XJ%5BY'L'gposZJ'_%2CKjieldqJ('value~typeZ%22genomic%01%22~qj_ZYXVQPNLKJ4*_>)

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

### Text

The `text` mark is designed to display textual labels. For example, gene names and nucleobases can be displayed with a `text` mark.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/text_example.png" width="800" alt="text_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%0A%205~tleZBasic%20Marks%3A%20Text4%0A5sub~tleZTutorial%20Examples4%0A5layoutZlinear4%0A5arrangement9('direc~onZver~cal42columnSizes9800)%2C%0A5tracks9%5Bj%20jI(**'data9(*5urlZhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2F~leset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQXJ~leset'*Nmetadata9(*5Jhiglass-mul~vecXrowZbaseXcolumnZposi~onXvalueZcountXcategoriesO%2C*5startZstartXendZendXbin916*)%2C**'markZtext4*'yKcount42Jquan~ta~ve'Nstyle9('textStrokeWidth90Nstretch9true%2C*'xKstart%2242axisZtop'NxeKend%22'Ncolor9(*5fieldZbaseXJnominalXdomainO*NtextKbase42Jnominal')jI)j%5D%0A)*jI%205%20'4'%2C5%2029!%20I%20%20JtypeZK9('fieldZN)%2C*'O9%5B'A42T42G42C'%5DX4*5Z!2j%0AI~ti%2242Jgenomic%01%22~jZXONKJI9542*_>)

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

### Link

The `link` mark is designed to show connections between chromosomes using an arc that connects two genomic intervals.

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/link_example.png" width="800" alt="link_example">  

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(9%20'YBasic%20MXks%3A%20LRkjsubYTutorial%20ExamplesjlayoutHlReXjXrangementQ'directionHverticalD'columnSizes4800A9'track_9*(UNQq'urlHhttps%3AJraw.githubusercontent.cZ%2Fsehilyi%2FgemRi-Nsets%2Fmaster%2FN%2Fcircos-segdup-edited.txtI'VHcsvIKFOHc2I'WFO_'s1D'e1D's2D'e2'%5D3A%0AUmXkHlRkDGP%20V%0A3J%20bRd%20visual%20channels%20to%20correspondRg%20N%20fOsUxQqCs1I7I63~eQCe1D7'~1QqCs2I7I63~1eQCe2D7'A%0A3Gstyles%20of%20PUstrokeQ'valueHsteelblue'AUstyleQ'circulXLRk4true)9*)9%5D%0A)*%20%2039**4!%205'%2C6'dZaRQKH1'Aq'axisHtop'7'VHW9%0A*A)%2CC'fOHD5%20GJ%20specify%20H4'I5qJ%2F%2FK'chrZosZeNdataOieldPthe%20mXkQ4(RinU3'VtypeWgenZicXarYtitleHZom_s4%5Bj59'q3*~AUx%01~qj_ZYXWVURQPONKJIHGDCA976543*_>)


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

### Triangle
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/master/src/core/mark/triangle.ts)  

Gosling supports three types of triangle marks: `triangle-l`, `triangle-r`, `triangle-d`

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=>)

<!-- ### Brush
### Glyph -->
