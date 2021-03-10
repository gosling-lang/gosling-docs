One `track` is the minimum visualization unit in Gosling.
Multiple `tracks` with the same [`layout`]((https://github.com/gosling-lang/gosling-docs/blob/master/docs/Layout.md)) compose a `view` and a Gosling visualization can have multiple `views`.

In Gosling, users can create an advanced visual interface by composing different `tracks` and `views`.
We use the `alignment` property to specify how we compose several `tracks`. 
We use the `arrangement` property to specify how we compose several `views`.

```javascript
{
  "arrangement": "parallel"// how to arrange multiple views 
  "views": [
    {
      // a single view can contain multiple tracks
      "alignment": "stack", // alignment property specifies how several tracks are aligned
      "tracks": [
        {/** track 1 **/},
        {/** track 2 **/},
        ...
      ]
    },
    {
      /** view **/
    }
    ...
  ]
}
```


- [Align Multiple Tracks](#align-multiple-tracks)
- [Arrange Multiple Views](#arrange-multiple-views)
- [Inherit Property in Nested Structure](#inherit-property-in-nested-structure)

## Align Multiple Tracks
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L213)

The `alignment` propoerty allow users to either `"overlay"` or `"stack"` several tracks.


When setting `alignment` as `"overlay"`, multiple `tracks` are overlaid on top of one other. 
When setting `alignment` as `"stack"`, multiple `tracks` are vertically concantenated.
<table>
    <tr>
        <td>  
        <pre>
<code>
{
  "layout": "linear",
  "alignment": "stack",
  "tracks": [
    {/**track_1**/},
    {/**track_2**/}
  ]   
}
</code>
        </pre>
        </td>
        <td>
        <pre>
<code>
{
  "layout": "linear",
  "alignment": "overlay",
  "tracks": [
    {/**track_1**/},
    {/**track_2**/}
  ]   
}
</code>
        </pre>
        </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/alignment_stack.png" alt="stack tracks" width="300"/> </td>
        <td> <img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/alignment_overlay.png" alt="overlay tracks" width="300"/></td>
    </tr>
</table>

<table>
    <tr>
        <td>  
        <pre>
<code>
{
  "layout": "linear",
  "alignment": "stack",
  "tracks": [
    {/**track_1**/},
    {/**track_2**/},
    {/**track_3**/}
  ]   
}
</code>
        </pre>
        </td>
        <td>
        <pre>
<code>
{
  "layout": "circular",
  "alignment": "stack",
  "tracks": [
    {/**track_1**/},
    {/**track_2**/},
    {/**track_3**/}
  ]   
}
</code>
        </pre>
        </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/tracks_linear.png" alt="linear tracks" width="400"/> </td>
        <td> <img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/tracks_circular.png" alt="circular tracks" width="200"/></td>
    </tr>
</table>

Try it in the online editor:

[Line chart (line + point)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/dd5bd5aa70f2eb68f92f42788f046188>)

[Lollipop plot (bar + point)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/d94c24b086bb4f6e5af48af6ebad1ca2>)

[Ideogram (text + rect + triangle)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/90cc96ca5f199c78d8985e4c162c6788>)



Multiple `tracks` can compose one single `view`, which has the following properties:
|property|type|description|
|--|--|--|
| layout | string | specify the layout type of all children tracks, either "linear" or "circular" |
| spacing | number | specify the space between tracks|
| static | boolean | whether to disable [Zooming and Panning](https://github.com/gosling-lang/gosling-docs/blob/master/docs/User-Interaction.md#zooming-and-panning), default=false. | 
| assembly | string | currently support "hg38", "hg19", "hg18", "hg17", "hg16", "mm10", "mm9"| 
| xLinkingId | string | specify an ID for [linking multiple views](https://github.com/gosling-lang/gosling-docs/blob/master/docs/User-Interaction.md#linking-views)|
| centerRadius | number | specify the proportion of the radius of the center white space. A number between [0,1], default=0.3|


## Arrange Multiple Views
Goslings supports multi-view visualizations. How multiple views are arranged is controlled by the `arrangement` property.
```javascript
{
  "arrangement": "parallel",
  "views": [
    // one view is composed of tracks that share the same layout property (linear or circular)
    {
      "layout": "linear",
      "tracks": [...]
    },
    // One view can have a hierarchical structure. 
    // For example, the view below is composed of two sub-views
    {
      "arrangement": "serial",
      "views": [
        {
          "tracks": [...]
        },
        {
          "tracks": [...]
        }
      ]
    }
  ]
}
```

Gosling supports four types of arrangemet: `"parallel"`, `"serial"`, `"vertical"`, `"horizontal"`.
<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/multi_views.png" alt="arrangement of multiple views" width="700"/> </td>


## Inherit Property in Nested Structure 
<!-- ```javascript
{
  "tracks": [
     {/** single track **/},
     {/** single track **/},
     {  ..., // Shared track definition
        alignment: 'overlay', tracks: [...]
     },
  ]
}
```

```javascript
{
  "views": [
     {/** single view **/},
     {/** single view **/},
     {  arrangement: 'serial', views: [...]
     },
  ]
}

``` -->


One `track` can have a nested structure and contains children `tracks`. 
Each children `track` inherits the properties (e.g., `data`, `x`, and `y`) defined in the parent `track` unless these properties are redefined in this object.  

```javascript
{
  "tracks": [
    {
      // the parent track
      "data": ... , // specify data
      "x": ...,
      "y": ...,
      "color":...,
      "alignment": "overlay",
      "tracks": [
        // the children tracks
        // point mark and line mark have the same data, x, y, color encoding
        {
          "mark": "line", 
        },
        {
          "mark": "point", 
          // specify the size of point mark
          "size": {"field": "peak", "type": "quantitative", "range": [0, 6]} 
        }
      ]
    }
  ]
}
```

