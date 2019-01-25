function run() {
  var helper = Application("TimingHelper");
  if (!helper.scriptingSupportAvailable()) { throw "Scripting support requires a Timing Expert license. Please contact support via https://timingapp.com/contact to upgrade."; }
  var app = Application.currentApplication();
  app.includeStandardAdditions = true;
  helper.stopCurrentTask({"notification":true})
}