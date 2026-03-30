console.log(Js работает);
var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {

        var post = e.target.closest(".one-post");

        post.classList.toggle("folded");

        if (post.classList.contains("folded")) {
            e.target.innerHTML = "развернуть";
        } else {
            e.target.innerHTML = "свернуть";
        }

    });
}