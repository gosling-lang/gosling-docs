---
title: Composition
---

<!-- Overview -->
A **track** is a unit building block in Gosling which can be represented as a bar chart, a line chart, or an ideogram. For the concurrent analysis of multiple datasets, multiple tracks can be grouped into **views** and navigated synchronously. In other words, a view defines the genomic location for all the tracks it contains, and the tracks define the data to be visualized.

<!-- :pushpin: `mark + channel` :arrow_forward: `one track` :arrow_forward:`tracks` :arrow_forward: `one view` :arrow_forward: `views` :arrow_forward: `a multi-view visualization` -->

<!-- :pushpin: `a multi-view visualization` :arrow_forward: `views` :arrow_forward: `tracks` :arrow_forward: `mark+channel`   -->

<!-- Overview of Properties -->
In Gosling, you can compose multiple tracks and views in diverse ways using the following properties:

1. You can display genomic positions of a view either in Cartesian coordinates (**linear**) or in polar coordinates (**circular**) using the `layout` property.  
2. You can determine to either **overlay** or **stack** multiple tracks when composing them into a view using a `alignment` property.   
3. You use juxtapose multiple views in four different ways (i.e., **parallel**, **serial**, **vertical**, **horizontal**) using the `arrangement` property.

```javascript
{
  "arrangement": "parallel"// how to arrange multiple views 
  "views": [
    {
      // a single view can contain multiple tracks
      "layout": "circular", // specify the layout of a view
      "alignment": "stack", // specify how to align several tracks
      "tracks": [
        {/** track 1 **/},
        {/** track 2 **/},
        ...
      ]
    },
    {
      /** another view **/
    }
    ...
  ]
}
```


- [Specify the View Layout](#specify-the-view-layout)
- [Align Multiple Tracks in One View](#align-multiple-tracks-in-one-view)
- [Arrange Multiple Views](#arrange-multiple-views)
- [Inherit Property in Nested Structure](#inherit-property-in-nested-structure)


## Specify the View Layout

In each view, genomic coordinate can be represented in either a **circular** or **linear** layout. 

In the following figure the upper track is using a linear layout while the bottom one is a circular layout.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/linear_circular.png" alt="linear vs circular" width="600"/>    

Users can either specify the layout of all views in the root level

```javascript
{
    "layout": "linear", //specify the layout of all views
    "views":[...]
}
```

or  specify/override the layout of a certain view in its own definition

```javascript
{
    "layout": "linear", //specify the layout of all tracks in this view
    "tracks":[...]
}
```

To enable an easy switch, both `linear` and `circular` layout can be specified through `width` and `height`.  
**<a>Note</a>:** the meaning of `height` is different in `circular` and `linear` layout.  
A `linear` layout is controlled by the following properties:

| property | type   | description                   |
| -------- | ------ | ----------------------------- |
| width    | number | width (in pixel) of the view  |
| height   | number | height (in pixel) of the view |

A `circular` layout is controlled by the following properties:

| property     | type   | description                                                                     |
| ------------ | ------ | ------------------------------------------------------------------------------- |
| width        | number | width (in pixel) of the view                                                    |
| height       | number | you need to specify the height of each track to control the ratio of their ticknesses |
| centerRadius | number | `radius of the center white space` / `radius of the whole view`. default = 0.3  |

<!-- 
|              |        | <a> the below properties, if specified, will override the above properties </a> |
| outerRadius  | number | default = min(track.width, track.height) / 2                                    |
| innerRadius  | number | default = max(outerRadius - 80, 0)                                              |
| startAngle   | number | default = 0                                                                     |
| endAngle     | number | default = 360                                                                   |
 -->


## Align Multiple Tracks in One View
<!-- [:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L213) -->

The `alignment` propoerty allow users to either `"overlay"` or `"stack"` several tracks.


When setting `alignment` as `"overlay"`, multiple `tracks` are overlaid on top of others.
When setting `alignment` as `"stack"`, multiple `tracks` are vertically concantenated.
The default value of `alignment` is `"stack"`.

<img src="https://raw.githubusercontent.com/gosling-lang/gosling-docs/master/images/alignment.png" alt="alignment of multiple tracks" width="700"/> 

Multiple `tracks` can compose one single `view`, which has the following properties:

| property     | type    | description |
| ------------ | ------- | ------------|
| layout       | string  | specify the layout type of all tracks, either "linear" or "circular"   |
| alignment    | string  | specify how to align tracks, either "stack" or "overlay". default="stack"|
| spacing      | number  | specify the space between tracks in pixels (if `layout` is `linear`) or in percentage ranging from `0` to `100` (if `layout` is `circular`)                     |
| static       | boolean | whether to disable [Zooming and Panning](https://github.com/gosling-lang/gosling-docs/blob/master/docs/user-interaction.md#zooming-and-panning), default=false. |
| assembly     | string  | currently support "hg38", "hg19", "hg18", "hg17", "hg16", "mm10", "mm9"                                                                                         |
| linkingId    | string  | specify an ID for [linking multiple views](https://github.com/gosling-lang/gosling-docs/blob/master/docs/user-interaction.md#linking-views)                     |
| centerRadius | number  | specify the proportion of the radius of the center white space. A number between [0,1], default=0.3                                                             |
| width        | number  | required when setting `alignment: overlay`                                                                                                                      |
| height       | number  | required when setting `alignment: overlay`                                                                                                                      |



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

Both `view` and `track` supports nested structures: One `view` can have several children `views`, and one `track` can have several children `tracks`. Properties can be inherited from upper-level specifications or overwritten locally.

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

Use the nested structure if you want to use overlaid tracks inside stacked tracks.


Try examples in the online editor:

[Line chart (line + point)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/dd5bd5aa70f2eb68f92f42788f046188>)

[Lollipop plot (bar + point)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/d94c24b086bb4f6e5af48af6ebad1ca2>)

[Ideogram (text + rect + triangle)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/90cc96ca5f199c78d8985e4c162c6788>)
