[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/gosling.schema.ts#L278)

Advanced zooming technique, called Semantic Zooming, allows you to dynamically switch between visual representations upon zooming in and out. 

<!-- ![SemanticZoom](https://user-images.githubusercontent.com/9922882/108913415-ebe5a600-75f7-11eb-84a2-2536ae9e8e2c.gif) -->

<!-- [Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?full=false&spec=(X'titleN'Basic%20Semantic%20Zoom%20Example~X'subtitleN'Zoom%20in%20and%20out%20to%20see%20how%20different%20visual%20encoding%20can%20be%20applied%20depending%20on%20the%20zoom%20level~X'layoutN'linear~%20X'centerRadiusN0.5%2CX'tracksN%5BX*(X**'dataN(-'typeN'multivec~-'urlN'https%3A%2F%2Fresgen.io%2Fapi%2Fv1%2Ftileset_info%2F%3Fd%3DUvVPeLHuRDiYA3qwFlm7xQ~-'valueN'y~-'rowN'_~-'columnN'x~-'categoriesN%5B'_'%5D%2C-'binSizeN12X**)%25markN'rect~X**'x%26start%22xe%26end%22styleN('outlineN'black~%20'outlineWidthN1)%25widthN620%25heightN130%2C%0AX**'overlayN%5BKE79F00MJGO800000IjK57B4E9MJGO80000I%24O800000IjK029F73MJGO8000I%24O80000IjK0072B2MJGO800I%24O8000IjKD45E00MJGO80I%24O800IjKCB7AA7MJGO8I%24O80I*)-*%5D-)X**%5DX*)X%5D%0A)*%20%20-X***8*'targetN'mark~-***'thresholdN1000I%2C-***'measure!*'zoomLevel'-*J-**(-***'operationN'K-(-*'colorN('valueN'%23M')%2C-*'visibilityN%5BN!%20OT~-**X%0A*j*)-*%5D-)%2C~'%2C%22~%20'typeN'genomic')%25%24*)%2CJL%25%2CX**'%26N('fieldN'%01%26%25%24%22~jXONMKJI8-*_>) -->

For example, detailed information of nucleotide bases can be shown with textual labels when zoomed in while it can be switched to show the overall distribution of the bases using a stacked bar chart when zoomed out.

## Example: Sequence Visualization
<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/semantic_zoom_1.png" alt="semantic_zoom_fine" width="700">

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/semantic_zoom_0.png" alt="semantic_zoom_coarse" width="700">  

[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/aa231b87458369ea53d071ad59c81812>)

## Example: Cyto Band
<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/semantic_zoom_2.png" alt="semantic_zoom_coarse" height="60" width="700">  

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/semantic_zoom_3.png" alt="semantic_zoom_fine" height="60" width="700"> 

**Top**: only `rect` marks are represented; **Bottom:** `text` and `triangle` marks are presented when zooming in to show more details.  
[Try this example in the online editor](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/509f253bf1b815d225f593218ee13211>)


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