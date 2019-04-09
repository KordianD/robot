var age, nick, group, percentage, port, time
port = 5000;
time = 10;
user_id_gen = Math.ceil(Math.random() * 1e8);

function endFun() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/robot/end', true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    console.log({result: percentage, group: group, nick: nick, age: age});
    xhr.send(JSON.stringify({result: percentage, group: group, nick: nick, age: age}));
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            <!--window.alert(xhr.responseText);-->
            window.location.replace(xhr.responseText);
        }
    }
}

var xhr = new XMLHttpRequest();
xhr.open('GET', '/robot/config', true);
xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE) {
        var json = xhr.responseText;
        obj = JSON.parse(json);
        nick = obj['nick']
        age = obj['age']
        group = obj['group']
        var config = obj['config'];
        console.log(obj);
        config.forEach(parameter =>{
            if(parameter.name == 'port')
                port = parameter.value;
            else if(parameter.name == 'time')
                time = parameter.value;
        });
    }
}
xhr.send(null);

var mousedown_now, direction_now

$(function() {
    $(':button').on('touchstart mousedown', function() {
        direction_now = $(this).attr('id'),
        mousedown_now = 1
        return false;
    });
});

$(function() {
    $(':button').on('touchend mouseup', function() {
        direction_now = $(this).attr('id'),
        mousedown_now = 0
        return false;
    });
});

setInterval( function() {
    $.getJSON('http://0.0.0.0:' + port + '/control_robot', {
        direction: direction_now,
        mousedown: mousedown_now,
        user_id: user_id_gen
    });
}, 100)

