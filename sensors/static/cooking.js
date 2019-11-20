var overview = document.querySelector("#overview");
var ingredients = document.querySelector("#ingredients");
var steps = document.querySelector("#steps");
var stepItems = document.querySelectorAll("#steps article");
var message = document.querySelector("#message");


if ('getBattery' in navigator)  {
    // The Battery API is available
    navigator.getBattery().then(function(battery) {
        updateBattery(battery);  // on load
        battery.addEventListener("chargingchange", function() {
            updateBattery(battery); // when the user changes the status
        }); 
        battery.addEventListener("levelchange", function() {
            updateBattery(battery);
        });
    });

}

function updateBattery(battery) {
    if (!battery.charging) {
        if (battery.level<0.1) {
            showMessage("Battery Level Critical. You must charge your device");
        } else {
            showMessage("Consider charging your phone while cooking");
        }
    } 
}

function goOverview() {
    hide(ingredients);
    hide(steps);
    show(overview);
}

function goIngredients() {
    show(ingredients);
    hide(steps);
    hide(overview);
}

var currentStepIndex;
function goStep(stepNumber) {
    currentStepIndex = stepNumber;
    hide(ingredients);
    show(steps);
    hide(overview);

    for (var step of stepItems) {
        hide(step);
    }
    show(stepItems[stepNumber])
}

function goNextStep() {
    if (currentStepIndex==stepItems.length-1) {
        goStep(0);
    } else {
        goStep(currentStepIndex+1);
    }
}

function goPrevStep() {
    if (currentStepIndex>0) {
        goStep(currentStepIndex-1);
    }
}

function hide(element) {
    element.style.display = "none";
}
function show(element) {
    element.style.display = "block";
}

var timerOff;
function showMessage(text) {
    show(message);
    message.innerHTML = text;
    clearTimeout(timerOff);
    if ('vibrate' in navigator) {
        navigator.vibrate(200);
    }

    timerOff = setTimeout(function() {
        // Hide the message after 5s
        hide(message);
    }, 5000);
}

goOverview();
showMessage("Welcome! Use your finger or voice to manipulate");