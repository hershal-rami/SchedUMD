function showSemesters() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches('.semester-dropbtn')) {
        var dropdowns = document.getElementsByClassName("semester-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
            }
        }
    }
}
