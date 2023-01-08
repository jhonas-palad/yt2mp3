const secondsToMin = (seconds) => {
    return seconds / 60;
}

const formatVideoLength = (length) => {
    const strMinutes = secondsToMin(length).toString();
    var [minute, dec] = strMinutes.split('.');
    var seconds;
    if(dec){
        dec = '.' + dec;
        seconds = parseInt((parseFloat(dec) * 60)).toString();
    }else{
        seconds = '00';
    }
    

    return `${minute}:${seconds}`;
}