function getOS() {
  var os = "";
  if (navigator.appVersion.indexOf("Win") != -1 || navigator.userAgent.indexOf('Windows NT 6.2') > -1) os = "Windows";
  if (navigator.appVersion.indexOf("Mac") != -1) os = "Mac";
  if (navigator.appVersion.indexOf("X11") != -1 || navigator.appVersion.indexOf("Linux") != -1) os = "Linux";
  return os;
}

$(document).ready(function () {
  os = getOS();
  updateInstructionsURL(os);
  windows = $(".windows");
  // Show source code download for Linux distros.
  if (os == "Linux") {
    $('#latest .button').attr("href", $("#latest .Source").attr("href")).text("Download source code");
    $('#paraview .button').attr("href", $("#paraview .Source").attr("href")).text("Download source code")

    windows.hide();
  }
  else {
    osClass = "." + os

    $('#latest .button').attr("href", $("#latest " + osClass).attr("href")).append($('#latest ' + osClass).text());
    $('#paraview .button').attr("href", $("#paraview " + osClass).attr("href"));

  }
});
