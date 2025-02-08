fullScr="""
<div id="confirmButtonDiv" style="text-align:center; padding:20px;">
    <button onclick="goFullScreenParent()" style="padding:10px 20px; font-size:16px;">Confirm Full Screen</button>
</div>
<script>
function goFullScreenParent() {
    // Access the parent document from within the iframe
    var parentElem = window.parent.document.documentElement;
    if (parentElem.requestFullscreen) {
        parentElem.requestFullscreen().then(function() {
            // Hide the confirm button div after successfully entering full screen
            document.getElementById('confirmButtonDiv').style.display = 'none';
        }).catch(function(err) {
            console.log("Error enabling full-screen mode: " + err.message);
        });
    } else if (parentElem.mozRequestFullScreen) { 
        parentElem.mozRequestFullScreen();
        document.getElementById('confirmButtonDiv').style.display = 'none';
    } else if (parentElem.webkitRequestFullscreen) { 
        parentElem.webkitRequestFullscreen();
        document.getElementById('confirmButtonDiv').style.display = 'none';
    } else if (parentElem.msRequestFullscreen) { 
        parentElem.msRequestFullscreen();
        document.getElementById('confirmButtonDiv').style.display = 'none';
    }
}

function isParentFullScreen() {
    var parentDoc = window.parent.document;
    return !!(parentDoc.fullscreenElement || 
              parentDoc.webkitFullscreenElement || 
              parentDoc.mozFullScreenElement || 
              parentDoc.msFullscreenElement);
}

function setupFullScreenListener() {
    window.parent.document.addEventListener("fullscreenchange", function() {
        if(isParentFullScreen()){
            console.log("Parent document is now in full-screen mode.");
        } else {
            console.log("Parent document has exited full-screen mode.");
        }
    });
}

function setupVisibilityListener() {
    window.parent.document.addEventListener("visibilitychange", function() {
        if (window.parent.document.hidden) {
            console.log("User has switched tabs or minimized the window.");
        } else {
            console.log("User has returned to the tab.");
        }
    });
}
setupFullScreenListener();
setupVisibilityListener();
</script>
"""
