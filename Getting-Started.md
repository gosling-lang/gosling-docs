# Overview
We currently support three different ways of using Gosling.

1. Embed a Gosling component directly in a HTML file.
2. Use `<GoslingComponent/>` in a React app.
3. Use our online Editor to quickly visualize your own data without setting up anything.


```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="theme-color" content="lightgray" />
        <link rel="stylesheet" href="https://unpkg.com/higlass@1.11.3/dist/hglib.css">
    </head>

    <body>
        <div id="root"/>
        <script crossorigin type="text/javascript" src="https://unpkg.com/react@16/umd/react.development.js"></script>
        <script crossorigin type="text/javascript" src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
        <script crossorigin type="text/javascript" src="https://unpkg.com/pixi.js@5/dist/pixi.js"></script>
        <script crossorigin type="text/javascript" src="https://unpkg.com/gosling.js@0.0.24/dist/gosling.js"></script>
    </body>
    <script>
      gosling.embed(
        document.getElementById('root'),
        {
          "tracks": [
            {
              "data": {
                "url": "https://resgen.io/api/v1/tileset_info/?d=UvVPeLHuRDiYA3qwFlm7xQ",
                "type": "multivec",
                "row": "sample",
                "column": "position",
                "value": "peak",
                "categories": ["sample 1", "sample 2", "sample 3", "sample 4"]
              }
            }
          ]
        }
      );
    </script>
</html>
```

## Resources
- How to set up your own HiGlass server for private data exploration?
   - HiGlass Server: https://github.com/higlass/higlass-server
   - HiGlass Docker: https://github.com/higlass/higlass-docker
- To prepare your own HiGlass data
   - HiGlass docs for data preparation: https://docs.higlass.io/data_preparation.html
