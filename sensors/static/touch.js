document.addEventListener("touchstart", function(event) {
    var touches = event.touches;
    /*
        iPhone: 5 max touches
        Android: 10 max touches
        iPad: 11 max touches
    */
    if (touches.length==2) {
        goIngredients();
        if ('vibrate' in navigator) {
            navigator.vibrate([300, 200, 300, 200, 500]);
        }
    } else if (touches.length==3) {
        goStep(0);
    } else {
        for (var touch of touches) {
            var x = touch.clientX;
            var y = touch.clientY;
            var force = touch.force;  // 0 - 1
        }
    }
});

var gestureRecognizer = new Hammer(document);
gestureRecognizer.on("swipe", function(event) {
    if (event.direction==4) {
        goNextStep();
    } else if (event.direction==2) {
        goPrevStep();
    }
});