
    function isEmpty( el ){
        return !$.trim(el.html())
    }

    function setError(field_element,message,put_sign=true){
        field_element.append('<p class="help is-danger">' + message + '</p>');

        var input = field_element.find('.input');
        var control = input.closest('.control');
        input.addClass('is-danger');
        if(put_sign){
            control.addClass('has-icons-right');
            control.append('<span class="icon is-right has-text-danger"><i class="mdi mdi-alert-circle mdi-24px"></i></span>');
        }
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

                for(var i = 0; i<24;i++){
                    var value = i;
                    if(i<10)
                        value = '0'+value;

                    hours.append('<option value="' + value + '">' + value + '</option>');
                }

                for(var i = 0; i<4;i++){
                    var value = i*15;
                    if(value<10)
                        value = '0'+value;
                    minutes.append('<option value="' + value + '">' + value + '</option>');
                }
                minutes.append('<option value=59>59</option>');
            });   
        }
        var timers = $('.timepicker.control');
        
        //set events
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
                input.trigger('change');
            });

            minutes.on('change', function(){
                var input_value = input.val();
                if(input_value == ''){
                    input.val('00:'+ $(this).val());
                }
                var result = input.val().substr(0,3)+ $(this).val();
                input.val(result);
                input.trigger('change');
            });

            input.on('change keyup', function(){
                var hour = $(this).val().substr(0,2);
                var min = $(this).val().substr(3,2);

                minutes.val(min);
                hours.val(hour);
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

    function nextStep(b_steps){
        var steps = b_steps.find('.steps .step-items .step-item');
        for(var i = 0; i<steps.length-1;i++){
            var step = steps.eq(i);
            if(step.hasClass('is-active')){
                return setStepActive(b_steps,i+1);
            }
        }
    }

    function prevStep(b_steps){
        var steps = b_steps.find('.steps .step-items .step-item');
        for(var i = 1; i<steps.length;i++){
            var step = steps.eq(i);
            if(step.hasClass('is-active')){
                return setStepActive(b_steps,i-1);
            }
        }
    }

    function setStepActive(b_steps,index){
        var steps = b_steps.find('.steps .step-items .step-item');
        var content = b_steps.find('.step-content .step-item');
        
        content.hide();
        steps.removeClass("is-active");
        steps.removeClass("is-previous");

        for(var i = 0; i<=index;i++){
            var step = steps.eq(i);

            if(index == i){
                step.addClass("is-active");
                content.eq(i).show();
            }else{
                step.addClass("is-previous");
            }
        }
    }

    function focusElementInStep(el){
        var index = el.closest('.step-item').prevAll('.step-item').length;
        setStepActive(el.closest('.b-steps'),index);
    }

    function fixSteps(){
        $(".b-steps").each(function(){
            var steps = $(this).find('.steps .step-items .step-item');
            steps.on("click",function(){
                var index = $(this).prevAll('.step-item').length;
                setStepActive($(this).closest(".b-steps"),index);
            });
                
            $(this).find('.next-step').on("click",function(){
                nextStep($(this).closest(".b-steps"));
            });

            $(this).find('.prev-step').on("click",function(){
                prevStep($(this).closest(".b-steps"));
            });
        });
    }

    //Tables with class sortable
    function enableSort(){
        $('table.sortable').DataTable();
    }

    $(document).ready(function(){
        //alert("TEST");
        errorHandler();
        removeEmptySelectOptions();
        enableSort();
        fixTimer();
        fixSteps();
    });