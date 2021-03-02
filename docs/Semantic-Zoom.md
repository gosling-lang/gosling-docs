[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/gosling.schema.ts#L278)

Advanced zooming technique, called Semantic Zooming, allows you to dynamically switch between visual representations upon zooming in and out. 

![SemanticZoom](https://user-images.githubusercontent.com/9922882/108913415-ebe5a600-75f7-11eb-84a2-2536ae9e8e2c.gif)

[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(X'titleN'Basic%20Semantic%20Zoom%20Example~X'subtitleN'Zoom%20in%20and%20out%20to%20see%20how%20different%20visual%20encoding%20can%20be%20applied%20depending%20on%20the%20zoom%20level~X'layoutN'linear~%20X'centerRadiusN0.5%2CX'tracksN%5BX*(X**'dataN(-'typeN'multivec~-'urlN'https%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQ~-'valueN'y~-'rowN'_~-'columnN'x~-'categoriesN%5B'_'%5D%2C-'binSizeN12X**)%25markN'rect~X**'x%26start%22xe%26end%22styleN('outlineN'black~%20'outlineWidthN1)%25widthN620%25heightN130%2C%0AX**'overlayN%5BKE79F00MJGO800000IjK57B4E9MJGO80000I%24O800000IjK029F73MJGO8000I%24O80000IjK0072B2MJGO800I%24O8000IjKD45E00MJGO80I%24O800IjKCB7AA7MJGO8I%24O80I*)-*%5D-)X**%5DX*)X%5D%0A)*%20%20-X***8*'targetN'mark~-***'thresholdN1000I%2C-***'measure!*'zoomLevel'-*J-**(-***'operationN'K-(-*'colorN('valueN'%23M')%2C-*'visibilityN%5BN!%20OT~-**X%0A*j*)-*%5D-)%2C~'%2C%22~%20'typeN'genomic')%25%24*)%2CJL%25%2CX**'%26N('fieldN'%01%26%25%24%22~jXONMKJI8-*_>)

For example, detailed information of nucleotide bases can be shown with textual labels when zoomed in while it can be switched to show the overall distribution of the bases using a stacked bar chart when zoomed out.

## Example: Sequence Visualization
<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/semantic_zoom_1.png" alt="semantic_zoom_fine" width="700">

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/semantic_zoom_0.png" alt="semantic_zoom_coarse" width="700">  

[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(J'titleNExample%3A%20Semantic%20Zooming'V'subtitleNhide%25annotation%20and%20only%20show%20bar%20charts%20when%20zooming%20out'V'arrangement6(J*'directionNvertical'V*'columnSizes6800V*'rowSizes6180J)V'tracks6%5BJ*(JLdata6(5'urlNhttps%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DWipsnEDMStahGPpRfH9adA'BQtileset'J**)VLmetadata6(5Qhiglass-multivec'B'rowNbase'B'columnN%3C'valueNcount'B'categoriesjstartNstart'B'endNend'J**)V**%20'x6(5'U%3CQ%24B'domain6KB'axisNtop'J**)VLcolor6(5'Ubase'BQnominal'B'domainjlegend6trueJ**)VLy6%3BQquantitative')VLoverlay6%5B5(%2B)B(5*%2BB*'s%26~61)B*'stroke%3EXgtet'BY620I5L%221%235)B%2F%2F%25mark5(5*'dataTransform6(5Lfilter6%5B%3B'oneOf6%5B0%5DI'not6true)%5D5*)B*'markNtext'B*'x6(5LUstart'BLtypeN%24BLdomain6KBLaxisNtop'5*)B*'xe6('Uend'IQ%24)B*'color%3E*'y~670)BXless-than'BYN%7Cxe-x%7C'5**I'%223%23B*%20'text6('Ubase'IQnominal')B'style6(5LtextFontSize624BLtextS%2660BLtextFontWeightNbold'5)5)J**%5DJ*%20J*%20J*)J%5D%0A)*%20%205J***6!%20B%2C5I%2C%20J%0A*K('chromosomeN1'I'interval6%5B3000000I3000010%5D)L**'N6'Q'typeNUfieldNV%2CJX*'visibility6(5LoperationNYLmeasureNwidth'BLthresholdj6%5B'A'I'T'I'G'I'C'%5DB'~6('value%22transitionPadding6%230BLtargetNmark'5*)%24genomic'%25%20text%20%26trokeWidth%2B'markNbar'%3B('Ucount'I%3Cposition'B%3E~Nwhite')B%01%3E%3C%3B%2B%26%25%24%23%22~jYXVUQNLKJIB65*_>)

## Example: Cyto Band
<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/semantic_zoom_2.png" alt="semantic_zoom_coarse" height="60" width="700">  

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/semantic_zoom_3.png" alt="semantic_zoom_fine" height="60" width="700"> 

**Top**: only `rect` marks are represented; **Bottom:** `text` and `triangle` marks are presented when zooming in to show more details.  
[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(%3F'titleK'Example%3A%20Semantic%20ZoomingM%3F'subtitleK'Text%20and%20triangle%20marks%20will%20show%20when%20zooming%20in%20to%20provide%20more%20detailsM%3F'layoutK'linearM%3F'arrangementK(%0AjdirectionK'verticalM%0AjcolumnSizesK800%2C%0AjrowSizesK60%3F~%3F'tracksK%5B%3F*%3F*(%3FjdataK(J'urlK'https%3A%2F%2Fraw.githubusercontent.com%2Fsehilyi%2Fgemini-datasets%2Fmaster%2Fdata%2FUCSC.HG38.Human.CytoBandIdeogram.csvMJ'typeK'csvMJ'c%5EFieldK'C%5EMJ'genomicFieldsK%5B'chromStartVchromEnd'%5D%3F**~%3FjoverlayK%5BJ(J*'markK'rectMJ*%40C%5EMJ%22J*jchr1Q2Q3Q4Q5Q6Q7Q8Q9Q10Q11Q12Q13Q14Q15Q16Q17Q18Q19Q20Q21Q22QXQY'J**%5D%2C%7D'%23F6F6F6Vgray'%3D'xK(%60StartV%3CVaggregateK'min'~J*'xeK(%60EndVaggregateK'maxV%3C'~J*'strokeWidth%262~J*'stroke%26'gray'~J*%3BMJjmeasureK'zoomLevelMJjthresholdK3%2CJjtargetK'track'J*%2BtextMJ_Rtrue)%3D'textK('%24NameVtypeK'nominal'~J*%40StainMJ%22'gnegV%25%7D'blackVblackVblackVblackVwhiteVblack'%3D%3BMJjmeasureK'widthMJjthresholdK'%7Cxe-x%7CMJj%7F10%2CJjtargetK'mark'J*~J*'styleK('textStrokeWidthK0%2BrectMJ_Rtrue)%3D%40StainMJ%22'gnegV%25%7DJ*jwhiteMJ*j%23D9D9D9MJ*j%23979797MJ*j%23636363MJ*jblackMJ*j%23A0A0F2'J**%5DJ*%2Btriangle-rMJ_J***R%3E'qVnotKfalse)J**%7B1'%2Btriangle-lMJ_J***R%3E'pVnotKfalse)J**%7B1')J)%3F**%5D%2C%3FjxK(J%60StartMJ'%3CMJ'domainK('c%5EK'1'~J'axisK'top'%3F**~%3FjxeK(%60EndV%3C'~%3Fjsize%2620~%3Fjstroke%26'gray'~%3FjstrokeWidth%260.5~%3FjstyleK('outlineK'white'~%3FjvisibilityK(J'operationK'greater-thanMJ'measureK'widthMJ'thresholdK3%2CJ'%7F5%2CJ'targetK'mark'%3F**)%3F*)%3F%5D%0A)*%20%20J%3F***K!%20M'%2CQMJ*jchrR('%24StainVoneOfK%5B'acen'%5D%2C%20'notKVM%20'_*'dataTransformK(JjfilterK%5Bj**'~)%2C%22jtypeK'nominalMJjdomainK%5B%24fieldK'%25gpos25Vgpos50Vgpos75Vgpos100Vgvar'%5D%2C%26K('valueK%2B)J~J(J*'markK'%3B'visibilityK(JjoperationK'less-than%3CtypeK'genomic%3D%5DJ*~J*%3Efalse~J***('%24NameVincludeK%3F%0A*%40'colorK(Jj%24%5Ehromosome%60'%24chrom%7B%3D'color%26'%23B4010%7DJjrangeK%5B%7FtransitionPaddingK%01%7F%7D%7B%60%5E%40%3F%3E%3D%3C%3B%2B%26%25%24%22~j_VRQMKJ*_>)


Semantic zoom through `overlay` and `visibility`.
[`overlay`](#superposition) overlaps multiple marks on top of one other, thus allowing users to create different visualizations for the same data.
`visibility` controls the visibility of visual marks, thus allowing the switch between different visualizations based on the zoom level.

`visibility` is an array of object with the following properties:
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
    // overlay overlaps bar marks and text marks for the same data
    "overlay":[
      //bar marks always show
      {"mark": "bar"},
      //text marks only show when the width of mark is great than 20 
      {
        "mark": "text",
        "visibility": [{
          "operation": "greater-than",
          "measure": "width",
          "threshold": "20",
          "target": "mark"
        }] 
      }
    ]
  }]
}
```