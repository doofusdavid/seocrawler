$(document).ready(function() {
    var jurl = '../data.json';
    $.ajax({
        type: "GET",
        url: jurl,
        success: parseData,
        error: handleError,
        timeout: 3000
    });

});

function parseData(data) {
    console.log(data);
}

function handleError(jqXHR, textStatus, errorThrown) {
    console.log('Error')
    console.log('jqXHR: ', JSON.stringify(jqXHR, null, 2))
    console.log('status: ', textStatus)
    console.log('err: ', errorThrown)
}