
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
                if(a.is('[selected]')){
                    a.remove();
                    $(this).val($(this).children('option').first().val());
                    return;
                }
                a.remove();
            }
        });
    }

    //Timer related

    function hideTimerDropDown(el){
        var dropdown = el.children('.dropdown');
        dropdown.removeClass('is-active');
        el.find('.dropdown-menu').hide();
    }

    function showTimerDropDown(el){
        var dropdown = el.children('.dropdown');
        var menu = el.find('.dropdown-menu');
        menu.show();
        dropdown.addClass('is-active');
    }

    

    function fixTimer(addtimes=true){
        
        //Add times to options
        if(addtimes){
            var timers = $('.timepicker.control').each(function(){
                var selects = $(this).find('.control>.select>select');
                var hours = selects.first();
                var minutes = selects.last();
                console.log(minutes.html());

                for(var i = 0; i<24;i++){
                    hours.append('<option value="' + i + '">' + i + '</option>');
                }

                for(var i = 0; i<4;i++){
                    var value = i*15;
                    minutes.append('<option value="' + value + '">' + value + '</option>');
                }
            });   
        }
        var timers = $('.timepicker.control');
        
        //set as hide
        timers.each(function(){
            $(this).children('.dropdown').removeClass('is-active');
            //$(this).find('.background').hide();
            $(this).find('.dropdown-menu').hide();
            var selects = $(this).find('.control>.select>select');
            var hours = selects.first();
            var minutes = selects.last();
            var input = $(this).find('input');
            hours.on('change', function(){
                var input_value = input.val();
                if(input_value == ''){
                    input.val($(this).val() + ':00');
                }
                var result = $(this).val() + input.val().substr(2,3);
                input.val(result);
            });

            minutes.on('change', function(){
                var input_value = input.val();
                if(input_value == ''){
                    input.val('00:'+ $(this).val());
                }
                var result = input.val().substr(0,3)+ $(this).val();
                input.val(result);
            });

            input.on('change', function(){
                var hour = $(this).val().substr(0,2);
                var min = $(this).val().substr(3,2);

                minutes.val(min);
                hour.val(min);
            });
            
        });


        //Show if clicked
        timers.on('click',function(e){
            var dropdown = $(this).children('.dropdown');
            if(dropdown.hasClass('is-active')){
            }else{
                showTimerDropDown($(this));
            }
            e.stopPropagation();
        });

        //Hide if clicked outside
        $(document).click(function(){
            timers.each(function(){
                var dropdown = $(this).find(".dropdown");
                hideTimerDropDown($(this));
            });
        });

    }

    //Tables with class sortable
    function enableSort(){
        $('.sortable').DataTable();
    }

    $(document).ready(function(){
        //alert("TEST");
        errorHandler();
        removeEmptySelectOptions();
        enableSort();
        fixTimer();
    });