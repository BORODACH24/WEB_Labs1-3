const topButton = document.getElementById('toTop')
console.log(topButton)

window.addEventListener('scroll', () => {
    if(window.pageYOffset > 100){
        topButton.classList.add("active");
    }
    else{
        topButton.classList.remove("active");
    }
})

const menuButton = document.getElementById('menu-button')
const menu = document.getElementById('menu')
menuButton.addEventListener('click', () => {
    menu.classList.toggle("active");
    menuButton.classList.toggle("active");
})
