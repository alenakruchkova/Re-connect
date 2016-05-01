

$('.advenced').click(function(e){
     e.preventDefault();
    $('#panelAdv').toggle();
});
$('.plus1 a').click(function(e){
    e.preventDefault();
    if($(this).children('i').hasClass('glyphicon-plus')){
        $(this).children('i').removeClass('glyphicon-plus').addClass('glyphicon-minus');
    }
    else{
          $(this).children('i').removeClass('glyphicon-minus').addClass('glyphicon-plus');
    }
    $('.morePanel1').toggle();
});
$('.plus2 a').click(function(e){
    e.preventDefault();
    if($(this).children('i').hasClass('glyphicon-plus')){
        $(this).children('i').removeClass('glyphicon-plus').addClass('glyphicon-minus');
    }
    else{
          $(this).children('i').removeClass('glyphicon-minus').addClass('glyphicon-plus');
    }
    $('.morePanel2').toggle();
});
$('.plus3 a').click(function(e){
       e.preventDefault();
    if($(this).children('i').hasClass('glyphicon-plus')){
        $(this).children('i').removeClass('glyphicon-plus').addClass('glyphicon-minus');
    }
    else{
          $(this).children('i').removeClass('glyphicon-minus').addClass('glyphicon-plus');
    }
    $('.morePanel3').toggle();
});