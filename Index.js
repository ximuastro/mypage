$(function(){
    $('.js-modal-open').each(function(){
        $(this).on('click',function(){
            var target = $(this).data('target');
            var modal = document.getElementById(target);
            $(modal).fadeIn();
            return false;
        });
    });
    $('.js-modal-close').on('click',function(){
        $('.js-modal').fadeOut();
        return false;
    }); 
});

$(function(){
    var imgs = $("#slideshow > li");
    var imgLen = imgs.length;
    var count = 0;
    
    function changeImg(){
      imgs.removeClass("showSlide").eq(count).addClass("showSlide");
      count = (count + 1) % imgLen; 
    }
    
    setInterval(changeImg, 300); // 各画像の表示時間を1秒に設定
})
