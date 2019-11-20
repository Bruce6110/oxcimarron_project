

$("p").each(function() {
  
    let replacementP = $("<p />");
    let lines = $(this).text().split(".");
    let split = "";
    alert("HEY");
    $(lines).each(function() {
           split = this.trim().split(' ');
      
      var span;
          
      if (split[0] !== "") {
        span = $("<span />", {
          "text": this.trim() + ".",
          "data-wc": split.length
        });
      }
      
      replacementP.append(span);
    
    });
      
    $(this).replaceWith(replacementP);
    
  });