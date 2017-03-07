



function filterContent()
{
    var user = document.getElementById("langfilter").value;
    var contentA = document.getElementById("contentA");
    var contentB = document.getElementById("contentB");
    var contentC = document.getElementById("contentC");
    var contentN = document.getElementById("contentN");

    if(user=="A") {
      contentA.style.display="block";
      contentB.style.display="none";
      contentC.style.display="none";

      contentN.style.display="none";

    } else if (user=="B") {
        contentA.style.display="none";
        contentB.style.display="block";
        contentC.style.display="none";

        contentN.style.display="none";



    } else if (user=="C") {
        contentA.style.display="none";
        contentB.style.display="none";
        contentC.style.display="block";

        contentN.style.display="none";


    }
    else if (user=="N") {
       contentA.style.display="none";
       contentB.style.display="none";
       contentC.style.display="none";
       contentN.style.display="none";
     }
}
