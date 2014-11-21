/*var simulate = function(element, eventName) {
    console.log('simulated-click');
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
      simulate(elm, "click");
    } else {
      console.log('This is not a proctortrack enabled quiz');
      simulate(elm, "click");
    }
      simulate(elm, "click");
};
  document.getElementById("take_quiz_link").addEventListener('click', takeQuizClick, false);
*/
  if(document.getElementById("verificient-enabled-quiz")) {
    console.log('This is proctortrack enabled quiz');
    var elm = document.getElementById("take_quiz_link");
    elm.href = document.getElementById('verificient-enabled-quiz').href
    elm.setAttribute('data-method', 'get');
    }

if(document.getElementById('submit_quiz_button')) {
    console.log('page has submit button');
    //check if submit is clicked, ping back to the server about test session closing
    var quizSubmitted = function() {
        console.log('submit is clicked, pinging server to close test session');

    }
    document.getElementById("submit_quiz_button").addEventListener('click', quizSubmitted, false);
}

var globalPopup;
(function(){
   var iterate = function() {
    if(window.globalPopup) { 
     console.log('checking app running');
     $.ajax({
            url: 'https://127.0.0.1/lti/app_started/',
            success: function() {
              console.log('app is running');
            }, 
            error: function() {
                window.globalPopup = 0; 
                console.log('app is not running');
                ask = confirm('Warming : Proctortrack-app is not running, This attempt will not be graded.');
    //            if(ask) {
                    //end this attempt
     //               $("#submit_quiz_button").click();
      //          } else {
       //             window.globalPopup = 1;
        //        }
            }});
    }
   };
   if(document.getElementById('questions')) {
        window.globalPopup = 1;
          window.setInterval(iterate, 5000);
   }
})();
