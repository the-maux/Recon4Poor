#!/bin/bash

echo -e '
<!DOCTYPE html>
<html>
<title>JSFScan</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
* {
  box-sizing: border-box;
}

.myInput {
  background-image: url("/css/searchicon.png");
  background-position: 10px 12px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}

.myUL {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.myUL li a {
  border: 1px solid #ddd;
  margin-top: -1px; /* Prevent double borders */
  background-color: #f6f6f6;
  padding: 12px;
  text-decoration: none;
  font-size: 18px;
  color: black;
  display: block
}

.myUL li a:hover:not(.header) {
  background-color: #eee;
}

pre {
  background: #f4f4f4;
  border: 1px solid #ddd;
  border-left: 3px solid #2798e3;
  color: #666;
  page-break-inside: avoid;
  font-family: monospace;
  font-size: 15px;
  line-height: 1.6;
  margin-bottom: 1.6em;
  max-width: 100%;
  overflow: auto;
  padding: 1em 1.5em;
  display: block;
  word-wrap: break-word;
}

pre1 {
  background: #f4f4f4;
  border: 1px solid #ddd;
  border-left: 3px solid #e32727;
  color: #666;
  page-break-inside: avoid;
  font-family: monospace;
  font-size: 15px;
  line-height: 1.6;
  margin-bottom: 1.6em;
  max-width: 100%;
  overflow: auto;
  padding: 1em 1.5em;
  display: block;
  word-wrap: break-word;
}

a:focus {
  color:blue;
}

html,body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
</style>
<body class="w3-light-grey">

<!-- Top container -->
<div class="w3-bar w3-top w3-black w3-large" style="z-index:4">
  <button class="w3-bar-item w3-button w3-hide-large w3-hover-none w3-hover-text-light-grey" onclick="w3_open();"><i class="fa fa-bars"></i>  Menu</button>
  <span class="w3-bar-item w3-right"><strong>JSFScan</strong></span>
</div>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-collapse w3-white w3-animate-left" style="z-index:3;width:300px;" id="mySidebar"><br>
  <div class="w3-container w3-row">
    <div class="w3-col s4">
      <img src="https://svgshare.com/i/TVH.svg" class="w3-circle w3-margin-left" style="width:46px">
    </div>
    <div class="w3-col s8 w3-bar">
      <span style="font-size:20px;">Welcome! to JSFScan Report.</span><br>
    </div>
  </div>
  <hr>
  <div class="w3-container">
    <h5><strong>Dashboard</strong></h5>
  </div>
  <div class="w3-bar-block">
    <a href="#" class="w3-bar-item w3-button w3-padding-16 w3-hide-large w3-dark-grey w3-hover-black" onclick="w3_close()" title="close menu"><i class="fa fa-remove fa-fw"></i>  Close Menu</a>
    <a href="#" class="w3-bar-item w3-button w3-padding link" onclick=openTable("page1");><i class="fa fa-users fa-fw" ></i> All JavaScript Links</a>
    <a href="#" class="w3-bar-item w3-button w3-padding link" onclick=openTable("page2");><i class="fa fa-eye fa-fw"></i>  Live JavaScript Links</a>
    <a href="#" class="w3-bar-item w3-button w3-padding link" onclick=openTable("page3");><i class="fa fa-users fa-fw"></i>  Endpoints</a>
    <a href="#" class="w3-bar-item w3-button w3-padding link" onclick=openTable("page4");><i class="fa fa-user-secret fa-fw"></i>  Secrets</a>
    <a href="#" class="w3-bar-item w3-button w3-padding link" onclick=openTable("page5");><i class="fa fa-list fa-fw"></i>  Wordlist</a>
    <a href="#" class="w3-bar-item w3-button w3-padding link" onclick=openTable("page6");><i class="fa fa-address-card fa-fw"></i>  Variables</a>
    <a href="#" class="w3-bar-item w3-button w3-padding link" onclick=openTable("page7");><i class="fa fa-bank fa-fw"></i>  DOM XSS</a>
    <a href="#" class="w3-bar-item w3-button w3-padding link" onclick=openTable("page8");><i class="fa fa-history fa-fw"></i>  JSFiles For Manualy Testing</a>
    <br><br>
  </div>
</nav>


<!-- Overlay effect when opening sidebar on small screens -->
<div class="w3-overlay w3-hide-large w3-animate-opacity" onclick="w3_close()" style="cursor:pointer" title="close side menu" id="myOverlay"></div>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:300px;margin-top:43px;">


  <body id="page">

    <div class="w3-container report" id="page1" style="display: none; padding-top:22px">
    <h4><b><i class="fa fa-dashboard"></i> All JavaScript Links</b></h4> ' >>report.html

echo -e " <input class='myInput' type='text' id='myInput1' onkeyup=\"myFunction('myInput1', 'myUL1')\" placeholder="Search.." title="Search">
    <div class="w3-responsive w3-card-4">
      <ul id=\"myUL1\" class=\"myUL\">" >>report.html

jslinks=./jsfile_links.txt
if [ -f "$jslinks" ]; then
  cat ./jsfile_links.txt | while read link; do echo -e "<li><a href="$link">$link</a></li>" >>report.html; done
else
  echo -e "<li><a href=" #">No Jslinks Links Found For Target</a></li>" >> report.html
fi

echo -e '
      </ul>
    </div>
    </div>' >>report.html

echo -e '
    <div class="w3-container report" id="page2" style="display: none; padding-top:22px">
      <h4><b><i class="fa fa-dashboard"></i> Live JavaScript Links</b></h4> ' >>report.html

echo -e " <input class='myInput' type='text' id='myInput2' onkeyup=\"myFunction('myInput2', 'myUL2')\" placeholder="Search.." title="Search">
    <div class="w3-responsive w3-card-4">
      <ul id=\"myUL2\" class=\"myUL\">" >>report.html

live_jslinks=./live_jsfile_links.txt
if [ -f "$live_jslinks" ]; then
  cat ./live_jsfile_links.txt | while read link; do echo -e "<li><a href="$link">$link</a></li>" >>report.html; done
else
  echo -e "<li><a href=" #">No Jslinks Links Found For Target</a></li>" >> report.html
fi

echo -e '
      </ul>
    </div>
    </div>' >>report.html

echo -e '
    <div class="w3-container report" id="page3" style="display: none; padding-top:22px">
      <h4><b><i class="fa fa-dashboard"></i> Endpoints</b></h4>' >>report.html

echo -e "<div class="w3-responsive w3-card-4"><pre1><strong>Press Ctrl + F to Search!</strong></pre1></div>
    <div class="w3-responsive w3-card-4">
      <ul id=\"myUL3\" class=\"myUL\">" >>report.html

endpoints=./endpoints.txt
if [ -f "$endpoints" ]; then
  echo -e "<pre><code>$(cat ./endpoints.txt | grep -Ev "Usage|Error")</code></pre>" >>report.html
else
  echo -e "<li><a href=" #">No Jslinks Links Found For Target</a></li>" >> report.html
fi

echo -e '
      </ul>
    </div>
    </div>' >>report.html

echo -e '

      <div class="w3-container report" id="page4" style="display: none; padding-top:22px">
        <h4><b><i class="fa fa-dashboard"></i> Secrets</b></h4>' >>report.html

echo -e " <div class="w3-responsive w3-card-4"><pre1><strong>Press Ctrl + F to Search!</strong></pre1></div>
  <div class="w3-responsive w3-card-4">
      <ul id=\"myUL4\" class=\"myUL\">" >>report.html

jslinksecret=./jslinksecret.txt
if [ -f "$jslinksecret" ]; then
  echo -e "<pre><code>$(cat ./jslinksecret.txt)</code></pre>" >>report.html
else
  echo -e "<li><a href=" #">No Jslinks Links Found For Target</a></li>" >> report.html
fi

echo -e '
      </ul>
    </div>
    </div>' >>report.html

echo -e '
        <div class="w3-container report" id="page5" style="display: none; padding-top:22px">
          <h4><b><i class="fa fa-dashboard"></i> Wordlist</b></h4>' >>report.html

echo -e " <div class="w3-responsive w3-card-4"><pre1><strong>Press Ctrl + F to Search!</strong></pre1></div>
    <div class="w3-responsive w3-card-4">
      <ul id=\"myUL5\" class=\"myUL\">" >>report.html

jswordlist=./jswordlist.txt
if [ -f "$jswordlist" ]; then
  echo -e "<pre><code>$(cat ./jswordlist.txt)</code></pre>" >>report.html
else
  echo -e "<li><a href=" #">No Jslinks Links Found For Target</a></li>" >> report.html
fi

echo -e '
      </ul>
    </div>
    </div>' >>report.html

echo -e '

          <div class="w3-container report" id="page6" style="display: none; padding-top:22px">
            <h4><b><i class="fa fa-dashboard"></i> Variables</b></h4>' >>report.html

echo -e " <div class="w3-responsive w3-card-4"><pre1><strong>Press Ctrl + F to Search!</strong></pre1></div>
    <div class="w3-responsive w3-card-4">
      <ul id=\"myUL6\" class=\"myUL\">" >>report.html

js_var=./js_var.txt
if [ -f "$js_var" ]; then
  echo -e "<pre><code>$(cat ./js_var.txt | sed -r "s/\x1B\[([0-9]{1,3}(;[0-9]{1,2})?)?[mGK]//g")</code></pre>" >>report.html
else
  echo -e "<li><a href=" #">No Jslinks Links Found For Target</a></li>" >> report.html
fi

echo -e '
      </ul>
    </div>
    </div>' >>report.html

echo -e '
            <div class="w3-container report" id="page7" style="display: none; padding-top:22px">
              <h4><b><i class="fa fa-dashboard"></i> DOM XSS</b></h4>' >>report.html

echo -e " <div class="w3-responsive w3-card-4"><pre1><strong>Press Ctrl + F to Search!</strong></pre1></div>
    <div class="w3-responsive w3-card-4">
      <ul id=\"myUL7\" class=\"myUL\">" >>report.html

dom_xss=./domxss_scan.txt
if [ -f "$dom_xss" ]; then
  echo -e "<pre><code>$(cat ./domxss_scan.txt)</code></pre>" >>report.html
else
  echo -e "<li><a href=" #">No Jslinks Links Found For Target</a></li>" >> report.html
fi

echo -e '
      </ul>
    </div>
    </div>' >>report.html

echo -e '
              <div class="w3-container report" id="page8" style="display: none; padding-top:22px">
                <h4><b><i class="fa fa-dashboard"></i> JSFiles For Manualy Testing</b></h4>' >>report.html

echo -e " <input class='myInput' type='text' id='myInput8' onkeyup=\"myFunction('myInput8', 'myUL8')\" placeholder="Search.." title="Search">
    <div class="w3-responsive w3-card-4">
      <ul id=\"myUL8\" class=\"myUL\">" >>report.html

live_jslinks=./live_jsfile_links.txt
if [ -f "$live_jslinks" ]; then
  cat ./live_jsfile_links.txt | while read link; do echo -e "<li><a href="$link" target="_blank" >$link</a></li>" >>report.html; done
else
  echo -e "<li><a href=" #">No Jslinks Links Found For Target</a></li>" >> report.html
fi

echo -e '
      </ul>
    </div>
    </div>' >>report.html

echo -e '
  </body>
  

  <!-- Footer -->
  <footer class="w3-container w3-padding-16 w3-theme-dark">
    <h4>JSFScan</h4>
    <p>Developed with <i class="fa fa-heart"></i> by <a href="https://github.com/KathanP19/JSFScan.sh" target="_blank">KathanP19</a></p>
  </footer>

  <!-- End page content -->
</div>

<script>
// Get the Sidebar
var mySidebar = document.getElementById("mySidebar");

// Get the DIV with overlay effect
var overlayBg = document.getElementById("myOverlay");

// Toggle between showing and hiding the sidebar, and add overlay effect
function w3_open() {
  if (mySidebar.style.display === "block") {
    mySidebar.style.display = "none";
    overlayBg.style.display = "none";
  } else {
    mySidebar.style.display = "block";
    overlayBg.style.display = "block";
  }
}

// Close the sidebar with the close button
function w3_close() {
  mySidebar.style.display = "none";
  overlayBg.style.display = "none";
}

function myFunction(Input, Id) {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById(Input);
    filter = input.value.toUpperCase();
    ul = document.getElementById(Id);
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function openTable(tablename) {
  var i;
  var x = document.getElementsByClassName("report");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  document.getElementById(tablename).style.display = "block";
}

</script>

</body>
</html>
' >>report.html
