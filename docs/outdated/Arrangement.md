A single visualization is called a 'track' in Gosling, and multiple tracks can be specified as an array in a `tracks` property.

```javascript
{
  "tracks":[
    {...}, // each object specifies a track 
    {...},
    ...
  ]
}
```

Using arrangement options supported in Gosling, you can juxtapose and superpose tracks in a flexible way.

# Grid-Based Arrangement
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L20)  

Using a `arrangement` property, you can specify a grid arrangement of multiple tracks. Each track listed in a `tracks` property will be positioned in a cell one by one. You can use a `span` property in a track definition to make the track being positioned across multiple cells in the grid. For example, `span: 2` make a track positioned across two cells.

| property                | type                        | description                                                                                                                                    |
| ----------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| arrangement.direction   | `string`                    | **Required**, the layout direction of all tracks (either `vertical`   or `horizontal`)                                                         |
| arrangement.wrap        | `number`                    | specify the number of tracks at each row (when `direction:horizontal`) or at each column (when `direction:vertical`). default value = infinite |
| arrangement.rowSizes    | `number` \| `Array<number>` | specify the height of each row in pixels                                                                                                       |
| arrangement.rowGaps     | `number` \| `Array<number>` | specify the gap between two rows in pixels                                                                                                     |
| arrangement.columnSizes | `number` \| `Array<number>` | specify the width of each column in pixels                                                                                                     |
| arrangement.columnGaps  | `number` \| `Array<number>` | specify the gap between columns in pixels                                                                                                      |

<img src="https://github.com/gosling-lang/gosling.js/wiki/images/layout_demo.png" alt="layout demo" width="400">

<!-- is it possible that several tracks under one layout have different type (linear and circular) -->

# Superposition
[:link: source code](https://github.com/gosling-lang/gosling.js/blob/43626eaf21417bf36128a405dceeaa6ee00d0851/src/core/Gosling.schema.ts#L213)


A `superpose` property enables you to overlay multiple tracks/marks on top of each other. `superpose` is an array of objects, and each object specifies one visual mark. Each visual mark inherits the properties (e.g., `data`, `x`, and `y`) defined in the corresponding track definition unless these properties are redefined in this object.  

```javascript
{
  "tracks": [
    {
      "data": ... , // specify data
      "x": ...,
      "y": ...,
      "color":...,
      "superpose": [
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

Try it in the online editor:

[Line chart (line + point)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/dd5bd5aa70f2eb68f92f42788f046188>)

[Lollipop plot (bar + point)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/d94c24b086bb4f6e5af48af6ebad1ca2>)

[Ideogram (text + rect + triangle)](<https://gosling-lang.github.io/gosling.js/?gist=wangqianwen0418/90cc96ca5f199c78d8985e4c162c6788>)

<!-- TODO: add channel.flip, channel.grid and other properties  -->

