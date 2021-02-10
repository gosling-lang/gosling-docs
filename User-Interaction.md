# Zooming and Panning
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/gosling.schema.ts#L7)

Each visualization in Gosling supports the Zooming and Panning interaction.
Users can zoom in/out a visualization using the scrolling up/down actions.
Users can pan by clicking on the visualization and then drag it in the desired direction.

Zooming and panning are controlled through the `static` property, which has a default value of `false`.
When `static = true`, zooming and panning are disabled.
Users can set the `static` property of all tracks at the root level or specify it in a single track definition. 
```javascript
{
  "static": true, //disable zoom & pan for all tracks
  "tracks": [
    {
      "static": false, // enable zoom & pan for this track
      ...
    },
    {
      ...
    },
    ...
  ]
}
```


# Semantic Zooming
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/gosling.schema.ts#L278)

Advanced zooming technique, called Semantic Zooming, allows you to dynamically switch between visual representations upon zooming in and out. For example, detailed information of nucleotide bases can be shown with textual labels when zoomed in while it can be switched to show the overall distribution of the bases without the text labels when zoomed out.

> Sehi: I will add an example with gene annotation <=> density plot

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_1.png" alt="semantic_zoom_fine" width="700">

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_0.png" alt="semantic_zoom_coarse" width="700">  

[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(J'titleNExample%3A%20Semantic%20Zooming'V'subtitleNhide%25annotation%20and%20only%20show%20bar%20charts%20when%20zooming%20out'V'arrangement6(J*'directionNvertical'V*'columnSizes6800V*'rowSizes6180J)V'tracks6%5BJ*(JLdata6(5'urlNhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DWipsnEDMStahGPpRfH9adA'BQtileset'J**)VLmetadata6(5Qhiglass-multivec'B'rowNbase'B'columnN%3C'valueNcount'B'categoriesjstartNstart'B'endNend'J**)V**%20'x6(5'U%3CQ%24B'domain6KB'axisNtop'J**)VLcolor6(5'Ubase'BQnominal'B'domainjlegend6trueJ**)VLy6%3BQquantitative')VLsuperpose6%5B5(%2B)B(5*%2BB*'s%26~61)B*'stroke%3EXgtet'BY620I5L%221%235)B%2F%2F%25mark5(5*'dataTransform6(5Lfilter6%5B%3B'oneOf6%5B0%5DI'not6true)%5D5*)B*'markNtext'B*'x6(5LUstart'BLtypeN%24BLdomain6KBLaxisNtop'5*)B*'xe6('Uend'IQ%24)B*'color%3E*'y~670)BXless-than'BYN%7Cxe-x%7C'5**I'%223%23B*%20'text6('Ubase'IQnominal')B'style6(5LtextFontSize624BLtextS%2660BLtextFontWeightNbold'5)5)J**%5DJ*%20J*%20J*)J%5D%0A)*%20%205J***6!%20B%2C5I%2C%20J%0A*K('chromosomeN1'I'interval6%5B3000000I3000010%5D)L**'N6'Q'typeNUfieldNV%2CJX*'visibility6(5LoperationNYLmeasureNwidth'BLthresholdj6%5B'A'I'T'I'G'I'C'%5DB'~6('value%22transitionPadding6%230BLtargetNmark'5*)%24genomic'%25%20text%20%26trokeWidth%2B'markNbar'%3B('Ucount'I%3Cposition'B%3E~Nwhite')B%01%3E%3C%3B%2B%26%25%24%23%22~jYXVUQNLKJIB65*_>)

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_2.png" alt="semantic_zoom_coarse" height="60" width="700">  

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/semantic_zoom_3.png" alt="semantic_zoom_fine" height="60" width="700"> 

**Top**: only `rect` marks are represented; **Bottom:** `text` and `triangle` marks are presented when zooming in to show more details.  
[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%3F'titleK'Example%3A%20Semantic%20ZoomingM%3F'subtitleK'Text%20and%20triangle%20marks%20will%20show%20when%20zooming%20in%20to%20provide%20more%20detailsM%3F'layoutK'linearM%3F'arrangementK(%0AjdirectionK'verticalM%0AjcolumnSizesK800%2C%0AjrowSizesK60%3F~%3F'tracksK%5B%3F*%3F*(%3FjdataK(J'urlK'https%3A%2F%2Fraw.githubusercontent.com%2Fsehilyi%2Fgemini-datasets%2Fmaster%2Fdata%2FUCSC.HG38.Human.CytoBandIdeogram.csvMJ'typeK'csvMJ'c%5EFieldK'C%5EMJ'genomicFieldsK%5B'chromStartVchromEnd'%5D%3F**~%3FjsuperposeK%5BJ(J*'markK'rectMJ*%40C%5EMJ%22J*jchr1Q2Q3Q4Q5Q6Q7Q8Q9Q10Q11Q12Q13Q14Q15Q16Q17Q18Q19Q20Q21Q22QXQY'J**%5D%2C%7D'%23F6F6F6Vgray'%3D'xK(%60StartV%3CVaggregateK'min'~J*'xeK(%60EndVaggregateK'maxV%3C'~J*'strokeWidth%262~J*'stroke%26'gray'~J*%3BMJjmeasureK'zoomLevelMJjthresholdK3%2CJjtargetK'track'J*%2BtextMJ_Rtrue)%3D'textK('%24NameVtypeK'nominal'~J*%40StainMJ%22'gnegV%25%7D'blackVblackVblackVblackVwhiteVblack'%3D%3BMJjmeasureK'widthMJjthresholdK'%7Cxe-x%7CMJj%7F10%2CJjtargetK'mark'J*~J*'styleK('textStrokeWidthK0%2BrectMJ_Rtrue)%3D%40StainMJ%22'gnegV%25%7DJ*jwhiteMJ*j%23D9D9D9MJ*j%23979797MJ*j%23636363MJ*jblackMJ*j%23A0A0F2'J**%5DJ*%2Btriangle-rMJ_J***R%3E'qVnotKfalse)J**%7B1'%2Btriangle-lMJ_J***R%3E'pVnotKfalse)J**%7B1')J)%3F**%5D%2C%3FjxK(J%60StartMJ'%3CMJ'domainK('c%5EK'1'~J'axisK'top'%3F**~%3FjxeK(%60EndV%3C'~%3Fjsize%2620~%3Fjstroke%26'gray'~%3FjstrokeWidth%260.5~%3FjstyleK('outlineK'white'~%3FjvisibilityK(J'operationK'greater-thanMJ'measureK'widthMJ'thresholdK3%2CJ'%7F5%2CJ'targetK'mark'%3F**)%3F*)%3F%5D%0A)*%20%20J%3F***K!%20M'%2CQMJ*jchrR('%24StainVoneOfK%5B'acen'%5D%2C%20'notKVM%20'_*'dataTransformK(JjfilterK%5Bj**'~)%2C%22jtypeK'nominalMJjdomainK%5B%24fieldK'%25gpos25Vgpos50Vgpos75Vgpos100Vgvar'%5D%2C%26K('valueK%2B)J~J(J*'markK'%3B'visibilityK(JjoperationK'less-than%3CtypeK'genomic%3D%5DJ*~J*%3Efalse~J***('%24NameVincludeK%3F%0A*%40'colorK(Jj%24%5Ehromosome%60'%24chrom%7B%3D'color%26'%23B4010%7DJjrangeK%5B%7FtransitionPaddingK%01%7F%7D%7B%60%5E%40%3F%3E%3D%3C%3B%2B%26%25%24%22~j_VRQMKJ*_>)


Semantic zoom through `superpose` and `visibility`.
[`superpose`](#superposition) overlaps multiple marks on top of one other, thus allowing users to create different visualizations for the same data.
`visibility` controls the visibility of visual marks, thus allowing the switch between different visualizations based on the zoom level.

`visibility` is an object with the following properties:
| properties  | type  | description|   
|---|---|---|
|target| string| **required**, support "track" \| "mark" |
| measure | string | **required**, support "width"\|"height"\|"zoomLevel".|
| threshold | "\|xe-x\|" \| number | **required**, when using `number`, the unit of a number is pixel with `width` and `height` measures while it is a base pair (bp) with `zoomLevel` |
| operation |  string | **required**, specify the logical operation to conduct between `threshold` and the `measure` of `target`<br/> > :"greater-than", "gt", "GT",<br/> < : "less-than", "lt", "LT", <br/> ≥ : "greater-than-or-equal-to", "gtet", "GTET"), <br/> ≤ : "less-than-or-equal-to", "ltet", "LTET"  |
  | conditionPadding | number | buffer px size of width or height when calculating the visibility, default = 0 |
| transitionPadding | number | buffer px size of width or height for smooth transition, default = 0 |

The `visibility` of corresponding marks are decided by whether the `measure` of `target` and the `threshold` satisfy the `operation`.

For example, in the code below, text marks only show when the width (`measure`) of the mark (`target`) is great-than (`operation`) 20 (`threshold`).

```javascript
{
  // example of semantic zoom: show text marks when zooming in

  "tracks":[{
    "data":...,
    "x": ...,
    "y": ...,
    // superpose overlaps bar marks and text marks for the same data
    "superpose":[
      //bar marks always show
      {"mark": "bar"},
      //text marks only show when the width of mark is great than 20 
      {
        "mark": "text",
        "visibility": {
          "operation": "greater-than",
          "measure": "width",
          "threshold": "20",
          "target": "mark",
          
        }  
      }
    ]
  }]
}
```

<!-- ## Tooltip
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L168) -->

# Linking Views
[:link: source code](ttps://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L328)

When two tracks are linked, the zooming and panning performed in one track will be automatically applied to the linked track. 

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%0AOlayout!6linear%5E%0AOarrangementC('direction!6vertical%5E6columnSizesC800%2C6rowSizesC200)%2C%0AOtracksC%5B%24E%22Gj%2Bb%40M3%5E%23%204%3Eline%25bNX*OaxKa%26*GZGrowBGcolorB%2C6%3CT%3B%2C%24E%22Gj%2Bb%40M2%3Earea%25bNX*OaxKthe%20same%26%20as%20the%20first%20track*GZGrowBGcolorB~%3CT%3B%0A%20%20%5D%0A)*J%20O%20'9%5E*OBC('field!%23%5E6Nnominal'C!%20Ehttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DUvVPeLHuG)%2C*'J%0A%20%20%20%20Kis!6top9linkingID!6link1'%20%2F%2F%20assign%20Mpeak9categoriesC%5B'sample%201%5E%23%20Ntype!6O%206TstrokeC('%40white'GstrokeWidthC('Xgenomic9domainC('chromosome!62')%2CZyC('field!6peak%5E6Nquantitative'b!6position9jmetadataC(*ONhiglass-multivec%22RDiYA3qwFlm7xQ9Ntileset'*%236sample%24J(*'dataC(*Ourl!6%25%5E*'xC(*Ofield%26%20linking%20id%2B9row!%239column%3BvalueC0.5)J)%3ClegendCtrueG%3E'%5D*Gmark!6%40value!6%5E'%2C%01%5E%40%3E%3C%3B%2B%26%25%24%23%22jbZXTONMKJGECB96*_>)

Users can link two tracks by assigning the same `linkingID` to the `x` channel of the two tracks.
```javascript
{
  "tracks":[
    // track A
    {
      "data": ...,
      "mark": "rect",
      "x": {
        ..., // other properties of x channel
        "linkingID": "a unique string" // assign a linking id for the track A
      }
    },
    // track B
    {
      "data": ...,
      "mark": "point",
      "x": {
        ..., // other properties of x channel
        "linkingID": "a unique string" // the same linking id links track A and track B
      }
    },
    ... // other tracks
  ]
}
```

# Brushing and Linking
Users can use **brushing** to select a subset of the data items using a rectangle. Users can modify the left and right edge of the rectangle to modify the selection. The selected data items can be linked to data items in another track.

[Try it in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(W'title~Example%3A%20Brushing%20and%20Linking'%2CW'layout~linear'%2CW'arrangement5('direction~vertical'O'columnSizes5800O'rowSizes5200ZW'tracks5%5B%229uRN*JXM%23G%24MK1'%25*Z*C**%2F%2F%20create%20a%20rectangle%20brush*'superpose5%5B*4()O%2F%2F%20this%20dummy%20object%20cannot%20be%20removed*4('mark~rect-brush'O*4'x5('T)6color5('value!'steelBlue')*4)*%5DW4Z%229uRN*JXM%23G%24MK1'O'interval5%5B200000000O220000000%5D%256T*Z*C*'opacity!('value51)W4)W%5D%0A)*W444%20%205!%206%2C*4'9'https%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DUvVPeLHC'y5('field~peak'O'type~quantitative'ZGories5%5B'sample%201'%5D*Z*'mark~line'%2CJ'metadata5(*4'type~higlass-multivec'Ktype~genomic'6domain5('chromosome~M~position'6NDiYA3qwFlm7xQ'6type~tileset'*ZO%2C%20TlinkingID~linking-with-brush'W%0A4X6row~sample'6columnZ)%2C~5'%22W4(*'data5(*4'url5%23value~peak'6categ%24*'x5(*4'field%25)6axis~top'%01%25%24%23%22~ZXWTONMKJGC9654*_>)

```javascript
{
  "tracks":[
    // track A
    {
      "data": ...,
      "mark": "line",
      ..., 

      // create a rectangle brush
      "superpose": [
        {}, // this dummy object cannot be removed
        {
          "mark": "rect-brush", 
          "x": {"linkingID": "linking-with-brush"}, // assign a unique id to the brush
          "color": {"value":"steelBlue"}
        }
      ]
    },
    // track B
    {
      "data": ...,
      "mark": "point",
      "x": {
        ..., // other properties of x channel
        "linkingID": "a unique string" // the same linking id links track B and the brush in track A
      }
    },
    ... // other tracks
  ]
}
```