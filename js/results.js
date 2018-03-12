$(document).ready(function() {
    var jurl = 'data.json';
    $.ajax({
        type: "GET",
        url: jurl,
        success: parseData,
        error: handleError,
        timeout: 3000
    });
    initAccordion();
});

function parseData(data) {
    console.log(data);
    $.each(data, function(key, value) {
        pageURL = "<h4 class='accordion-toggle'>" + key + "</h4>";
        pageData = "<div class='accordion-content'>" + value + "</div>";
        $('#accordion').append(pageURL);
        $('#accordion').append(pageData);
    });
}

function handleError(jqXHR, textStatus, errorThrown) {
    console.log('Error')
    console.log('jqXHR: ', JSON.stringify(jqXHR, null, 2))
    console.log('status: ', textStatus)
    console.log('err: ', errorThrown)
}

function initAccordion() {
    $('#accordion').find('.accordion-toggle').click(function() {
        //Expand or collapse this panel
        $(this).next().slideToggle('fast');

        //Hide the other panels
        $(".accordion-content").not($(this).next()).slideUp('fast');
    });
}