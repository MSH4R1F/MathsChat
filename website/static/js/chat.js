var socket;
$(document).ready(function() {
    // Connect to server
    var socket = io();

    // Event handler for new connections
    // Callback function is executed when a new connection with the server is established
    // When user connects emit to server with message joined
    socket.on('connect', function() {
        socket.emit('joined', {});
    });
    // Receiving status message which shows whether user joined or left
    socket.on('status', function(data) {
        // Add message to chat messages
        $('#chat-msg').append("<div class='message'><p class = 'meta'><span>" + data.time + "</span></p><p class='text'>" + data.msg + "</p>");
        // scrollTop property gets or sets the number of pixels that an element's content is scrolled vertically.
        var element = document.getElementById("chat-msg");
        element.scrollTop = element.scrollHeight;
    });
    // Receiving user list to add to users
    socket.on('userList', function(data) {
        console.log(data.msg);
    });

    socket.on('message', function(data) {
        console.log(data);
        if (data.sender == "true") {
            $('#chat-msg').append("<div class='message-container sender'><div class = 'message'> <p class = 'meta'> " + data.name + " <span>" + data.time + "</span></p><p class='text'>" + data.msg + "</p></div></div>");
            var element = document.getElementById("chat-msg");
            renderMathInElement(element, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\(', right: '\\)', display: false },
                    { left: '\\[', right: '\\]', display: true }
                ],
                // • rendering keys, e.g.:
            });
            element.scrollTop = element.scrollHeight;

        } else {

            $('#chat-msg').append("<div class='message-container recipient'><div class = 'message'><p class = 'meta'> " + data.name + " <span>" + data.time + "</span></p><p class='text'>" + data.msg + "</p></div></div>");
            var element = document.getElementById("chat-msg");
            renderMathInElement(element, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\(', right: '\\)', display: false },
                    { left: '\\[', right: '\\]', display: true }
                ],
                // • rendering keys, e.g.:
            });
            element.scrollTop = element.scrollHeight;

        }
    });

    $('#msg').keypress(function(e) {

        var code = e.keyCode || e.which;
        if (code == 13) {
            text = $('#msg').val();
            $('#msg').val('');
            console.log(text);
            socket.emit('text', { msg: text });
        }
    });
});

function leave_room() {
    socket.emit('leave', {}, function() {
        socket.disconnect();
        window.location.href = "{{ url_for(views.home)) }}";
    });
};

function scrollSmoothToBottom(id) {
    var div = document.getElementById(id);
    $("#" + id).animate({
            scrollTop: div.scrollHeight - div.clientHeight,
        },
        500
    );
}