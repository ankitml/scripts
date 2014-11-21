var simulate = function(element, eventName) {
    var options = extend(defaultOptions, arguments[2] || {});
    var oEvent, eventType = null;

    for (var name in eventMatchers)
    {
        if (eventMatchers[name].test(eventName)) { eventType = name; break; }
    }

    if (!eventType)
        throw new SyntaxError('Only HTMLEvents and MouseEvents interfaces are supported');

    if (document.createEvent)
    {
        oEvent = document.createEvent(eventType);
        if (eventType == 'HTMLEvents')
        {
            oEvent.initEvent(eventName, options.bubbles, options.cancelable);
        }
        else
        {
            oEvent.initMouseEvent(eventName, options.bubbles, options.cancelable, document.defaultView,
            options.button, options.pointerX, options.pointerY, options.pointerX, options.pointerY,
            options.ctrlKey, options.altKey, options.shiftKey, options.metaKey, options.button, element);
        }
        element.dispatchEvent(oEvent);
    }
    else
    {
        options.clientX = options.pointerX;
        options.clientY = options.pointerY;
        var evt = document.createEventObject();
        oEvent = extend(evt, options);
        element.fireEvent('on' + eventName, oEvent);
    }
    return element;
};


var takeQuizClick = function(e) {
    e.preventDefault();
    e.stopPropagation();
        var elm = document.getElementById("take_quiz_link");
        elm.removeEventListener('click', takeQuizClick, false);
    if(document.getElementById("verificient-enabled-quiz")) {
      console.log('This is a proctortrack enabled quiz');
        elm.href = document.getElementById('verificient-enabled-quiz').href
        elm.setAttribute('data-method', 'get');
    } else {
      console.log('This is not a proctortrack enabled quiz');
    }
      simulate(elm, "click");
};
  document.getElementById("take_quiz_link").addEventListener('click', takeQuizClick, false);
