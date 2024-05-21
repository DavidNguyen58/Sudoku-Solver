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
    <th class="square"><input name="row${i}8"></th>
    </tr>`
}
