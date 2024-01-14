
# Nebulos API

Easy to use Python API, implement your own Image & Text APIs with ease.

Made with Flask in Python

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/mom-made-pizza-rolls.svg)](https://forthebadge.com)





## Endpoints

#### Text API

Use text APIs
```http
GET /api/text/${category}
```

| Type     | Description                |
 :------- | :------------------------- |
 `string` | **Required**. Name of category to fetch |
 
```http
GET /api/text/categories
```

| Type     | Description                |
 :------- | :------------------------- |
 `string` | List all Image Categories |

#### Image API
Use image APIs
```http
GET /api/images/${category}
```

| Type     | Description                |
 :------- | :------------------------- |
 `string` | **Required**. Name of category to fetch |
 
```http
GET /api/image/categories
```

| Type     | Description                |
 :------- | :------------------------- |
 `string` | List all Image Categories |


## Documentation

[Documentation](https://api.nebulos.pro:3000/)


## Installation

Install Nebulos-API

```bash
git clone https://github.com/FILMA0010/Nebulos-API.git
cd Nebulos-API
pip install -r requirements.txt
```
    
## Execute

To execute this project run

```bash
python main.py
```


## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```


## License

[Apache](https://github.com/FILMA0010/Nebulos-API/blob/main/LICENSE)

[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)
##### Linux Ubuntu 22.04
#####  Linux Ubuntu 23.04
#####  Linux Debian 10
##### Python 3.10.12
