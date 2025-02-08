fullScr ="""
<!DOCTYPE html>
<html>
<head>
    <script>
    function goFullScreen() {
        var elem = document.documentElement;
        if (elem.requestFullscreen) {
        elem.requestFullscreen();
        } else if (elem.mozRequestFullScreen) { /* Firefox */
        elem.mozRequestFullScreen();
        } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
        elem.webkitRequestFullscreen();
        } else if (elem.msRequestFullscreen) { /* IE/Edge */
        elem.msRequestFullscreen();
        }
        document.getElementById('fullscreenButton').style.display = 'none';
    }
    
    </script>
</head>
<body>
    <button id="fullscreenButton" onclick="goFullScreen()" style='padding:10px 20px; font-size:16px;'>Confirm Fullscreen</button>
</body>
</html>
"""

fullScr1='''
<div id="confirmButtonDiv" style="text-align:center; padding:20px;">
    <button onclick="goFullScreen()" style="padding:10px 20px; font-size:16px;">Confirm Full Screen</button>
</div>
<script>
    function goFullScreen() {
        var elem = document.documentElement;
        if (elem.requestFullscreen) {
        elem.requestFullscreen();
        } else if (elem.mozRequestFullScreen) { /* Firefox */
        elem.mozRequestFullScreen();
        } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
        elem.webkitRequestFullscreen();
        } else if (elem.msRequestFullscreen) { /* IE/Edge */
        elem.msRequestFullscreen();
        }
        document.getElementById('fullscreenButton').style.display = 'none';
    }
    
    </script>
    '''
