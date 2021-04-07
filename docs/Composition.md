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


When setting `alignment` as `"overlay"`, multiple `tracks` are overlaid on top of others.
When setting `alignment` as `"stack"`, multiple `tracks` are vertically concantenated.
The default value of `alignment` is `"stack"`.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/alignment.png" alt="alignment of multiple tracks" width="700"/> 

Multiple `tracks` can compose one single `view`, which has the following properties:
|property|type|description|
|--|--|--|
| layout | string | specify the layout type of all tracks, either "linear" or "circular" |
| alignment | string | specify how to align tracks, either "stack" or "overlay". default="stack" |
| spacing | number | specify the space between tracks|
| static | boolean | whether to disable [Zooming and Panning](https://github.com/gosling-lang/gosling-docs/blob/master/docs/User-Interaction.md#zooming-and-panning), default=false. | 
| assembly | string | currently support "hg38", "hg19", "hg18", "hg17", "hg16", "mm10", "mm9"| 
| xLinkingId | string | specify an ID for [linking multiple views](https://github.com/gosling-lang/gosling-docs/blob/master/docs/User-Interaction.md#linking-views)|
| centerRadius | number | specify the proportion of the radius of the center white space. A number between [0,1], default=0.3|
| width | number | required when setting `alignment: overlay`|
| height | number | required when setting `alignment: overlay`|

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
<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/multi_views.png" alt="arrangement of multiple views" width="700"/> 


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
Both `view` and `track` supports nested structures: one `view` can have several children `views` and one `track` can have several children `tracks`. Properties can be inherited from upper-level specifications or overwritten locally.

```javascript
// nested structures in views
{
  "arrangement": "parallel",
  "views": [
    {/** view **/ }, 
    {/** view **/ }, 
    {
      // a view with children views
      "arrangement": "parallel",
      "views": [...]
    }
  ]
}
```

```javascript
// nested structures in tracks
{
  "alignment":"overlay",
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
It is recommended to use nested tracks ONLY IF a user wants to use overlaid tracks inside stacked tracks.


Try examples in the online editor:

[Line chart (line + point)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/dd5bd5aa70f2eb68f92f42788f046188>)

[Lollipop plot (bar + point)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/d94c24b086bb4f6e5af48af6ebad1ca2>)

[Ideogram (text + rect + triangle)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/90cc96ca5f199c78d8985e4c162c6788>)
