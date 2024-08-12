const screen = document.getElementById("display-target");

for (let i = 1; i <= 9; i ++){
    screen.innerHTML += 
    `<tr class="align-middle text-center">
        <td class="square" id="row${i}1"><input name="row${i}1" maxlength="1" autocomplete="off"></td>
        <td class="square" id="row${i}2"><input name="row${i}2" maxlength="1" autocomplete="off"></td>
        <td class="square" id="row${i}3"><input name="row${i}3" maxlength="1" autocomplete="off"></td>
        <td class="square" id="row${i}4"><input name="row${i}4" maxlength="1" autocomplete="off"></td>
        <td class="square" id="row${i}5"><input name="row${i}5" maxlength="1" autocomplete="off"></td>
        <td class="square" id="row${i}6"><input name="row${i}6" maxlength="1" autocomplete="off"></td>
        <td class="square" id="row${i}7"><input name="row${i}7" maxlength="1" autocomplete="off"></td>
        <td class="square" id="row${i}8"><input name="row${i}8" maxlength="1" autocomplete="off"></td>
        <td class="square" id="row${i}9"><input name="row${i}9" maxlength="1" autocomplete="off"></td>
    </tr>`
}
document.addEventListener('DOMContentLoaded', (event) => {
    const inputs = document.querySelectorAll('input');
    console.log(inputs)
    inputs.forEach(input => {
        input.addEventListener('focus', (e) => {
            e.target.select();
        });
        input.addEventListener('input', (e) => {
            e.target.value = e.target.value.replace(/[^0-9]/g, '');
        });
    });
});

const button = document.getElementById('button-submit')
const form = document.getElementById('form-submit')
button.addEventListener('click', async (event) => {
    event.preventDefault();
    let data = {}
    for (var i = 0; i < form.elements.length; i++) {
        var element = form.elements[i];
        if (element.name !== ""){
            let r = element.name.substring(3, 5);
            let v = element.value;
            data[r] = v;
        }
    }
    const res = await fetch(
        "http://127.0.0.1:5000",
        {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
        },
            body: JSON.stringify(data)
        }
    );
    if (!res.ok) {
        const message = `An error has occured: ${res.status}`;
        throw new Error(message);
    }
    const sol = await res.json()
    console.log(sol)
    render_solution(sol)
})

// render the solution on the screen
function render_solution(data){
    for(let i = 1; i <= 9; i++){
        for(let j = 1; j <= 9; j++){
            let index = `${i}${j}`
            const cell = document.getElementById(`row${index}`)
            cell.innerHTML = data[index]
        }
    }
}
// clear button
const clear = document.getElementById('button-clear')
// event listener for clear button
clear.addEventListener('click', (event) => {
    event.preventDefault();
    clear_board()
})
// function that clears the board
function clear_board(){
    for(let i = 1; i <= 9; i++){
        for(let j = 1; j <= 9; j++){
            let index = `${i}${j}`
            const cell = document.getElementById(`row${index}`)
            cell.innerHTML = `<input name="row${index}">`
        }
    }
}