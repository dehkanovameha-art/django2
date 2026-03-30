$(document).ready(function(){
console.log("jQuery работает");
});
    $('.one-post').hover(function(event){

        $(event.currentTarget)
            .find('.one-post-shadow')
            .animate({opacity: '0.1'}, 300);

    }, function(event){

        $(event.currentTarget)
            .find('.one-post-shadow')
            .animate({opacity: '1'}, 300);

    });
