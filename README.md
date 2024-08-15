# Sudoku Solver

## Project Description
The project aims at solving Sudoku by encoding the problem into propositional logic stored as a conjunction of disjunctions of literals. The knowledge will be then sent to the `maplechrono` in PySat for finiding the solution in propositional logic form. The program will then decode it and render the solution to the `index.html`.

## Install
``` sh
git clone
```
``` sh
pip install requirement.txt -r
```
## Usage
```
flask --app server run
```
## Test

## API

### POST /
* Content-Type: application/json
*   ```javascript
    // Sucessful Response
    {
        "11": $value,
        "12": $value,
        ...
        "99": $value
    }
    ```
    #### Error Handling
* HTTP 400 Bad Request
    - The problem can not be solved

## Reference
- https://users.aalto.fi/~tjunttil/2020-DP-AUT/notes-sat/solving.html
- https://sat.inesc-id.pt/~ines/publications/aimath06.pdf
- https://repository.vnu.edu.vn/bitstream/VNU_123/17423/1/00050007752.pdf

