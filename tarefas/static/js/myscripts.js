
    function isEmpty( el ){
        return !$.trim(el.html())
    }

    function errorHandler(){
        var els = $('.field > .help').each(function(){
            if(isEmpty($(this)))
                return;

            var input = $(this).closest('.field').find('.input');
            var control = input.closest('.control');
            control.addClass('has-icons-right');
            input.addClass('is-danger');
            control.append('<span class="icon is-right has-text-danger"><i class="mdi mdi-alert-circle mdi-24px"></i></span>');
        });
    }

    function removeEmptySelectOptions(){
        $('select').each(function(){
            var a = $(this).find('option:contains("---------")');
            if(a.length > 0){
                if(a.hasAttr('selected')){
                    a.remove();
                    $(this).val($(this).children('option').first().val());
                    return;
                }
                a.remove();
            }
        });
    }
    $(document).ready(function(){
        //alert("TEST");
        errorHandler();
        removeEmptySelectOptions();
    });