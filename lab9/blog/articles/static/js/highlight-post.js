$(document).ready(function(){
});
    $('.one-post').hover(function(event){

        $(event.currentTarget)
            .find('.one-post-shadow')
            .animate({opacity: '0.1'}, 300);
            concole.log("Навели на пост, currentTarget:", event.currentTarget);


    }, function(event){

        $(event.currentTarget)
            .find('.one-post-shadow')
            .animate({opacity: '0'}, 300);
            console.log

    });


