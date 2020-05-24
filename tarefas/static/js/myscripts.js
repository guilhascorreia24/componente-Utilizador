
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

    $(document).ready(function(){
        errorHandler();
    });