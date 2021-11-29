(function() {
    function rangeInputChangeEventHandler(e){
        var rangeGroup = $(this).attr('name');
            btn = $(`#${this.id}`)
            range = $(`#${this.id}_range`)
            label_val = parseInt($(btn).val())
            $(range).html(label_val);
    }

    function filter_ranges(e){
        let form_id = $(this).closest('form').attr('id');
            $(`#${form_id}`).submit();
    }

    function toggle_sidebar(e){
        e.preventDefault();
        $("#wrapper").toggleClass("menuDisplayed");
    }

$('input[type="range"]').on('input', rangeInputChangeEventHandler);
$('.range').on('mouseup', this, filter_ranges);
$('#menu-toggle').on('click', toggle_sidebar);

})();
