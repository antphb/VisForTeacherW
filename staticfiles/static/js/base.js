let arrow = document.querySelectorAll(".arrow");


arrow.forEach((arrow) => {
    arrow.addEventListener("click",(e) => {
        let arrowParent = e.target.parentElement.parentElement;
        console.log(arrowParent);
        arrowParent.classList.toggle("showMenu");
    })
});

let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".fa-bars");
sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close_menu");
})
