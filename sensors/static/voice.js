var voices;
    
window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition; 
    
var recognition;
    
if (window.SpeechRecognition==undefined) {
    alert("Speech Recognition API not available");   
} else {
    recognition = new SpeechRecognition()
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.onresult = function(event) { 
        if (event.type=="result") {
            for (var i=0; i<event.results.length; i++) {
                var confidence = parseInt(event.results[i][0].confidence*100);
                var text = event.results[i][0].transcript;
                if (text.indexOf("next step") > 0) {
                    goNextStep();
                } else if (text.indexOf("previous step") > 0) {
                    goPrevStep();
                } else if (text.indexOf("ingredients") > 0 ) {
                    goIngredients();
                }
                   
            }
        }
    };
    recognition.onerror = function(event) {
        console.log(event);
        
    }
};

document.querySelector("#btnVoice").addEventListener("click",
    function() {
        recognition.lang='en-US';
        recognition.start();
    })
