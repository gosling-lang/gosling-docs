We currently support the following three ways of using Gosling.

## 1. Use Online Editor
You can visit [Online Editor](gosling.js.org) to visualize your data directly in the website.

## 2. Embed Gosling Component in a HTML File
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
        <script crossorigin type="text/javascript" src="https://unpkg.com/gosling.js@0.0.26/dist/gosling.js"></script>
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

## 3. Use Gosling.js in React App

Install `gosling.js` and its dependent libraries:

```sh
yarn add gosling.js pixi.js react@16.13.1 react-dom@16.13.1
```

Add the following style sheets to your base `html` file:
```html
<head>
  ...
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://unpkg.com/higlass@1.11.3/dist/hglib.css">
</head>
```

Use the Gosling.js' react component to visualize your data:

```js
import { validateGoslingSpec, GoslingComponent } from "gosling.js";

...

// validate the spec
const validity = validateGoslingSpec(EXMAPLE_GOSLING_SPEC);

if(validity.state === 'error') {
    console.warn('Gosling spec is invalid!', validity.message);
    return;
}

...

function App() {
  
  ...

  return (
    <GoslingComponent
      spec={EXAMPLE_GOSLING_SPEC}
      compiled={(spec, vConf) => { /* Callback function when compiled */ }}
    />
  );
}
```

Please visit [gosling-react](https://github.com/gosling-lang/gosling-react) for more detailed instruction.

## Resources
- How to set up your own HiGlass server for private data exploration?
   - HiGlass Server: https://github.com/higlass/higlass-server
   - HiGlass Docker: https://github.com/higlass/higlass-docker
- How to prepare your own HiGlass data?
   - HiGlass docs for data preparation: https://docs.higlass.io/data_preparation.html
