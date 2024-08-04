const screen = document.getElementById("display-target");

for (let i = 1; i <= 9; i ++){
    screen.innerHTML += 
    `<tr class="align-middle text-center">
        <th class="square"><input name="row${i}1"></th>
        <th class="square"><input name="row${i}2"></th>
        <th class="square"><input name="row${i}3"></th>
        <th class="square"><input name="row${i}4"></th>
        <th class="square"><input name="row${i}5"></th>
        <th class="square"><input name="row${i}6"></th>
        <th class="square"><input name="row${i}7"></th>
        <th class="square"><input name="row${i}8"></th>
        <th class="square"><input name="row${i}9"></th>
    </tr>`
}

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
        const message = `An error has occured: ${response.status}`;
        throw new Error(message);
    }
    const sol = await res.json()
    console.log(sol)
})
