

function goToNewURL(url) {
    window.location.href = window.location.origin + url
}

function deleteInstance(pk) {
    let url = window.location.href.split('/')
    url = url.slice(0, url.length-2).join('/')
    window.location.href = url + "/delete/" + pk
}







